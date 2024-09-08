from OlympicsDataAnalysis import logger
from OlympicsDataAnalysis.config.configuration import ConfigurationManager
from OlympicsDataAnalysis.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        if not config.is_exists:
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion.copy_source_data()
            data_ingestion.extract_zip_file()
        else:
            logger.info("The folders and necessary files are already present")
