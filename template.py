import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format = '[%(asctime)s]: %(message)s:')
project_name = "OlympicsDataAnalysis"

file_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/app.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/preprocess/__init__.py",
    "requirements.txt",
    "setup.py",
    "research/olympic_notebook.ipynb",
]

for file_path in file_list:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir:
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f"Craeting directory {file_dir} for the file name: {file_name}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} is already present")
        
    