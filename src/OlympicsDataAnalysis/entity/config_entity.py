from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_data: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataPreprocessConfig:
    root_dir: Path
    preprocessed_data_file_path: Path