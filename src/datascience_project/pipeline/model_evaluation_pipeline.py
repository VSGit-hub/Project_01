from src.datascience_project import logger
from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.components.model_evaluation import ModelEvaluation

STAGE_NAME = "MODEL EVALUATION STAGE"

class ModelEvaluationPipelie:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()



if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
        obj=ModelEvaluationPipelie()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e