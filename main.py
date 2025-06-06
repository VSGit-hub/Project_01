from src.datascience_project import logger
from src.datascience_project.pipeline.data_ingestion_pipeline import DataIngestionTrainigPipelie
from src.datascience_project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience_project.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience_project.pipeline.model_trainer_pipeline import ModelTrainingPipelie
from src.datascience_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipelie


STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainigPipelie()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"\n>>>>>>>>>>STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>>>>STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<\n")
except Exception as e:
    raise e


STAGE_NAME = "MODEL TRAINING STAGE"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
    obj=ModelTrainingPipelie()
    obj.initiate_trina_model()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL EVALUATION STAGE"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
    obj=ModelEvaluationPipelie()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e