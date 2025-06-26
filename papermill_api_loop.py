import papermill as pm
years = [2022,2023,2026]
month = 12

for yearchoose in years:
    res = pm.execute_notebook(
        'date_print.ipynb',
        'date_print_{year}_{month}.ipynb',
        parameters= dict(year=yearchoose, month=month)
        )