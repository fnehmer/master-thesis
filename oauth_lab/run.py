from server.app import create_app


APP = create_app({
    # 'SECRET_KEY': 'secret',
    # 'OAUTH2_REFRESH_TOKEN_GENERATOR': True,
    # 'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    # 'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
})

if __name__ == '__main__':
    APP.debug = True
    APP.run()
