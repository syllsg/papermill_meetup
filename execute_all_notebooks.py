import papermill as pm
from pathlib import Path

for nb in Path('./test_folder').glob('*.ipynb'):
    pm.execute_notebook(
        input_path=nb,
        output_path=nb  # Path to save executed notebook
    )

















# Note: This script executes all Jupyter notebooks in the specified folder.
# Ensure that the folder './test_folder' exists and contains Jupyter notebooks.
# The output will overwrite the original notebooks with the executed results.
# You can change the output path if you want to save the executed notebooks elsewhere.
# Make sure to have papermill installed in your Python environment.
# You can install it using pip:
# pip install papermill
# This script assumes that the notebooks do not require any specific parameters.
# If parameters are needed, you can modify the pm.execute_notebook call accordingly.
# Example: pm.execute_notebook(input_path=nb, output_path=nb, parameters={'param_name': 'value'})
# This script is useful for batch processing multiple notebooks in a directory.
# It can be used for testing, data processing, or any other tasks defined in the notebooks.
# Make sure to handle any exceptions or errors that may arise during execution.
# You can add error handling to skip notebooks that fail to execute.
# For example, you can wrap the pm.execute_notebook call in a try-except block
# to catch and log any errors without stopping the execution of other notebooks.
# Example error handling:
# try:
#     pm.execute_notebook(input_path=nb, output_path=nb)
# except Exception as e:
#     print(f"Error executing {nb}: {e}")
# This will help you identify any issues with specific notebooks while still processing the rest.
# Ensure that the Jupyter environment is properly set up to run the notebooks.
# You may need to install additional dependencies required by the notebooks.
# This script can be run from the command line or as part of a larger automation workflow.
# Make sure to test it in a safe environment before running on important notebooks.
# You can also modify the script to log the execution status of each notebook.
# For example, you can print the name of each notebook before executing it.
# This will help you track the progress of the execution.
# Example logging:
# print(f"Executing notebook: {nb.name}")
# This will print the name of each notebook as it is being executed.
# You can also add a summary at the end to report how many notebooks were executed successfully and
# how many failed.
# Example summary:
# print(f"Executed {len(successful_notebooks)} notebooks successfully.")
# print(f"Failed to execute {len(failed_notebooks)} notebooks.")
# This will give you a clear overview of the execution results.
# You can also consider adding a timestamp to the output notebooks to indicate when they were executed.
# This can be done by adding a cell at the end of each notebook with the current date and time.
# Example:
# from datetime import datetime
# executed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# pm.execute_notebook(input_path=nb, output_path=nb, parameters={'executed_at': executed_at})
# This will help you keep track of when each notebook was last executed.
# Overall, this script provides a simple and effective way to execute multiple Jupyter notebooks in a
# specified folder, making it a useful tool for batch processing and automation tasks.
# Make sure to adapt the script to your specific needs and environment.
# You can also consider adding command-line arguments to specify the folder or output path dynamically.
# This can be done using the argparse module in Python.
# Example:
# import argparse
# parser = argparse.ArgumentParser(description='Execute all Jupyter notebooks in a folder.')
# parser.add_argument('folder', type=str, help='Path to the folder containing Jupyter notebooks.')
# args = parser.parse_args()
# for nb in Path(args.folder).glob('*.ipynb'):
#     pm.execute_notebook(
#         input_path=nb,
#         output_path=nb  # Path to save executed notebook                                      