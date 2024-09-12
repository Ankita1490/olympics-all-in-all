from distutils.command.config import config
from OlympicsDataAnalysis.config.configuration import ConfigurationManager
from OlympicsDataAnalysis.components.data_preprocessing import DataPreprocessing
from OlympicsDataAnalysis import logger

STAGE_NAME_02 = "Data Preprocess Stage"

class DataPreprocessPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        raw_data_path =config.config.data_ingestion.unzip_dir
        data_preprocessing_pipeline_config = config.get_data_preprocess_config()
        data_preprocessing = DataPreprocessing(raw_data_path, data_preprocessing_pipeline_config)
        preprocessed_df =data_preprocessing.preprocess()
        data_preprocessing.save_preprocessed_file(preprocessed_df)