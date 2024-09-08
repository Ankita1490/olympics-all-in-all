import os
import ensure
import yaml

from pathlib import Path
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox
from OlympicsDataAnalysis import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read and returns the content in the yaml file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Creates list of directories

    Args:
        path_to_directories (list): _description_
        verbose (bool, optional): _description_. Defaults to True.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
    



