from pathlib import Path
from typing import List
import pandas as pd
import os
import shutil

from OlympicsDataAnalysis import logger
from OlympicsDataAnalysis.entity.config_entity import DataPreprocessConfig


class DataPreprocessing:
    def __init__(self,raw_data_path: Path,data_preprocess_config:DataPreprocessConfig,):
        self.data_preprocessing_config = data_preprocess_config
        self.raw_data_path = raw_data_path
        self.althele_df = pd.read_csv(os.path.join(self.raw_data_path, "athlete_events.csv"))
        self.regions_df = pd.read_csv(os.path.join(self.raw_data_path, "noc_regions.csv"))
        
    def preprocess(self):
        """preprocess the data set"""       
        logger.info(f"data preprocessing started")
        preprocessed_df = (
            self.althele_df.query("Season == 'Summer'")
            .merge(self.regions_df, on = 'NOC', how = 'left')
        )
        preprocessed_df.drop_duplicates(inplace=True)        
        preprocessed_df = pd.concat([preprocessed_df, pd.get_dummies(preprocessed_df['Medal'], dtype= int)], axis= 1)
        logger.info("Proprocessed completed")
        return preprocessed_df
    
    def save_preprocessed_file(self, preprocessed_df:pd.DataFrame):        
        """
        Saves the preprocessed file in artifacts preprocessed directory
        """
        if not os.path.exists(self.data_preprocessing_config.preprocessed_data_file_path):
            preprocessed_df.to_csv(self.data_preprocessing_config.preprocessed_data_file_path)
            logger.info(f"Preproessed file is saved in the path {self.data_preprocessing_config.preprocessed_data_file_path} ")
            
            
            
            
            
        
        
        