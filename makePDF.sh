#!/bin/bash

#Generación de PDF compilando el archivo LaTeX con pdflatex
cd doc/text
pdflatex -synctex=1 -interaction=nonstopmode -shell-escape -output-directory=../../ project.tex
pdflatex -synctex=1 -interaction=nonstopmode -shell-escape -output-directory=../../ project.tex
cd ../../
rm {*.aux,*.lof,*.log,*.lol,*.lot,*.out,*.pyg,*.synctex.gz,*toc}
