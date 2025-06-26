import papermill as pm
year = 2026
res = pm.execute_notebook(
    'date_print.ipynb',
    'date_print_{year}.ipynb',
    parameters = dict(year=year)
)