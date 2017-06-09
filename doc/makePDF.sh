#!/bin/bash

#Generación de PDF compilando el archivo LaTeX con pdflatex
cd text
pdflatex -synctex=1 -interaction=nonstopmode -output-directory=../ project.tex
pdflatex -synctex=1 -interaction=nonstopmode -output-directory=../ project.tex
cd ..
rm {*.aux,*.lof,*.log,*.lol,*.lot,*.out,*.synctex.gz,*toc}
