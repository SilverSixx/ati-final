import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

notebook_path = 'train/steps.ipynb'

# Check if the notebook exists
if not os.path.exists(notebook_path):
    print(f"[ERROR] The notebook file '{notebook_path}' does not exist.")
else:
    print(f"[INFO] Loading notebook: {notebook_path}")

    # Open and read the notebook
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_content = nbformat.read(f, as_version=4)
        print("[INFO] Notebook loaded successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to load notebook: {e}")
        exit(1)

    # Set up the notebook execution processor
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    print("[INFO] Setting up the notebook execution processor.")

    # Try executing the notebook
    try:
        print(f"[INFO] Executing notebook: {notebook_path}...")
        ep.preprocess(notebook_content, {'metadata': {'path': './train'}})
        print("[INFO] Notebook executed successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to execute notebook: {e}")
        exit(1)

    print("[INFO] Execution complete. The notebook has been processed.")
