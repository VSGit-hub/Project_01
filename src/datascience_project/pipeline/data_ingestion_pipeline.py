from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.components.data_ingestion import DataIngestion
from src.datascience_project import logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainigPipelie:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.downloda_file()
        data_ingestion.extract_zipfile()


if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
        obj=DataIngestionTrainigPipelie()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

