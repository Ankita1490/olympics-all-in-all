import os
import urllib.request as request
import zipfile
import shutil
from OlympicsDataAnalysis import logger
from OlympicsDataAnalysis.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
    
    def copy_source_data(self):
        """
        Copy the zip file in the artifacts/data_ingestion folder
        """
        if not os.path.exists(self.data_ingestion_config.local_data_file):
            data_file_path = os.path.join(self.data_ingestion_config.root_dir, "olympics_data.zip")
            shutil.copy(self.data_ingestion_config.source_data, data_file_path)
            logger.info("file copied sucessfully")
        else:
            logger.info("file already exists")
            
    def extract_zip_file(self):
        """
        Extract zip file into the data directory
        """
        unzip_path = self.data_ingestion_config.unzip_dir
        if os.path.exists(self.data_ingestion_config.local_data_file):
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.data_ingestion_config.local_data_file,'r') as zip_ref:
                zip_ref.extractall(unzip_path)   
                logger.info("Extraction process completed")
        else:
            logger.info("unzipped file already exists")   
        