import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from src.datascience_project.entity.config_entity import ModelEvaluationConfig
from src.datascience_project.constants import *
from src.datascience_project.utils.common import save_json

import os
# os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/vbs.codestuff/Project_01.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"]="vbs.codestuff"
# os.environ["MLFLOW_TRACKING_PASSWORD"]="b7378850fb9748992f5d0f157e192c883bc11a78"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rsme = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rsme, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_X = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        trakcing_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_quantities = model.predict(test_X)

            (rsme, mae, r2) = self.eval_metrics(test_y, predicted_quantities)

            # Saving mertrics at local
            scores = {"rsme": rsme, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rsme", rsme)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if trakcing_url_type_store != 'file':
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")