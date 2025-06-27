import papermill as pm
from pathlib import Path
import sys

# Note: This script executes all Jupyter notebooks in the specified folder.

# Check if the folder exists
folder = Path('./execute_all_folder')
if not folder.exists() or not folder.is_dir():
    print("Error: Folder 'execute_all_folder' does not exist.")
    sys.exit(1)

else:
    for nb in folder.glob('*.ipynb'):
        pm.execute_notebook(
            input_path=nb,
            output_path=nb  # Path to save executed notebook
        )
# The output will overwrite the original notebooks with the executed results.