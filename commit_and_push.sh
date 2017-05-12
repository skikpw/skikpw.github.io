#!/bin/bash
echo commit i push pliku index.html
echo $1
git add . 
git commit -m "$1"
git push origin master

