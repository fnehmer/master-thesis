#!/bin/bash

docname="thesis"

echo Building...

pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -recorder ${docname}.tex
biber ${docname}
pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -recorder ${docname}.tex
pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -recorder ${docname}.tex

echo "Build completed!"
