import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name='datascience_project'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  # constructor will allow entire source folder to be imported like a package
    f"src/{project_name}/components/__init__.py",  # all components like data injestion, data transformation, model trainig, model eval will be in components   
    f"src/{project_name}/utils/__init__.py", # Will contain all generic function that may be used in the entire project
    f"src/{project_name}/utils/common.py",    #Continat funciton that are common to various components
    f"src/{project_name}/config/__init__.py",  #
    f"src/{project_name}/config/configuration.py",  #
    f"src/{project_name}/pipeline/__init__.py",  # Contain information regarding what are different pipelies are required
    f"src/{project_name}/entity/__init__.py",  #
    f"src/{project_name}/entity/config_entity.py",  #
    f"src/{project_name}/constants/__init__.py",  #
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/reseach.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating director {filedir}, for {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            
            pass
            logging.info(f"Creating empty filepath {filepath}")
    else:  
        logging.info(f"{filename} exits")


