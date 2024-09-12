from logging import root
import os
from OlympicsDataAnalysis.constants import CONFIG_FILE_PATH
from OlympicsDataAnalysis.entity.config_entity import DataIngestionConfig, DataPreprocessConfig
from OlympicsDataAnalysis.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.is_exists =os.path.exists(self.config.artifacts_root)
        if not self.is_exists:
            create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        is_exists = os.path.exists(config.root_dir)
        if not is_exists:
            create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_data= config.source_data,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
             
        )
        
        
        return data_ingestion_config
    
    def get_data_preprocess_config(self) -> DataPreprocessConfig:
        config = self.config.data_preprocesing
        is_exist = os.path.exists(config.root_dir)
        if not is_exist:
            create_directories([config.root_dir])
            
        data_preprocessing_config = DataPreprocessConfig(
            root_dir= config.root_dir,
            preprocessed_data_file_path= config.preprocessed_data_file_path
        )
        
        return data_preprocessing_config