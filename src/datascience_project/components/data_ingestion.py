import os
import urllib.request as requests
from src.datascience_project import logger
import zipfile

from src.datascience_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config) -> DataIngestionConfig:
        self.config=config

    def downloda_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = requests.urlretrieve(
                url=self.config.source_URL,
                filename= self.config.local_data_file
            ) 
            logger.info(f"{filename} downloaded! {headers}")
        else:
            logger.info(f"File already exits")

    def extract_zipfile(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
