import papermill as pm
from pathlib import Path
from datetime import datetime

# folder containing the notebooks to execute
folder = Path('./execute_all_folder')
# Get current date as YYYYMMDD
run_date = datetime.now().strftime("%Y%m%d")

# Example parameters to inject
params = {
    "month": 7,
    "year": 2026,
    "number_points": 30
}

for nb in Path('./execute_all_folder').glob('*.ipynb'):
    print(f"Executing notebook: {nb.name}")
    output_name = nb.stem+ f"_{run_date}" + nb.suffix
    pm.execute_notebook(
        input_path=nb,
        output_path=folder / output_name,
        parameters=params
    )
print(f"Executed {len(list(Path('./execute_all_folder').glob('*.ipynb')))} notebooks successfully.")

