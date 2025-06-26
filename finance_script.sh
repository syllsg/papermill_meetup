#!/bin/bash

set -eux

# activate  virtualenv 
source /home/sylvia/Code/perso/250624_meetup_python_papermill/.venv/bin/activate


# change to the directory of the script
cd $(dirname "${BASH_SOURCE[0]}")

for S in AAPL MSFT GOOG FB
do
        papermill -p symbol $S papermill_example2.ipynb papermill_${S}.ipynb
        jupyter-nbconvert --no-input --to html papermill_${S}.ipynb
done