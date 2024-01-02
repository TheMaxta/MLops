from fastapi import FastAPI
from pydantic import BaseModel
import mlflow
import mlflow.sklearn


app = FastAPI()


class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float



best_run = mlflow.search_runs(order_by=["metrics.accuracy desc"]).iloc[0]
best_run_id = best_run.run_id
best_model = mlflow.sklearn.load_model("runs:/" + best_run_id + "/model")




mlflow.sklearn.load_model("runs:/" + best_run_id + "/model")