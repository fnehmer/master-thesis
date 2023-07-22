import bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db: SQLAlchemy = SQLAlchemy()

class User(db.Model):
    """
    Standard User model

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user. Must be unique and non-null and the max length is 32.
        password (str): The hashed password of the user. Must be non-null.

    Methods:
        set_password(password: str) -> None:
            Sets the user's password after hashing it with a salt.
        
        verify_password(password: str) -> bool:
            Verifies if the provided password matches the user's stored hashed password.

    """
    __tablename__: str = 'user'

    id: Column = Column(Integer, primary_key=True)
    username: Column = Column(String, length=32, unique=True, nullable=False)
    password: Column = Column(String, length=72, nullable=False)

    def set_password(self, password) -> None:
        salt: bytes = bcrypt.gensalt()
        password_hash: bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = password_hash.decode('utf-8')

    def verify_password(self, password: str) -> bool:
        hashed_password: bytes = self.password.encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    
    def __str__(self) -> str:
        return f"id: {self.id}; username: {self.username}"
