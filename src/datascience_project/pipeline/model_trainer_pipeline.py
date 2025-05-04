from src.datascience_project import logger
from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.components.model_trainer import ModelTrainer

STAGE_NAME = "MODEL TRAINING STAGE"

class ModelTrainingPipelie:
    def __init__(self):
        pass

    def initiate_trina_model(self):
        config = ConfigurationManager()
        model_trainig_config = config.get_model_triner_config()
        model_train = ModelTrainer(config=model_trainig_config)
        model_train.train()



if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
        obj=ModelTrainingPipelie()
        obj.initiate_trina_model()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e