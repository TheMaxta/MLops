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

best_run_id = "74dc55a290244e508bac99dc12cc2c42"

mlflow.set_tracking_uri("http://127.0.0.1:5001")

model = mlflow.sklearn.load_model("runs:/" + best_run_id + "/model")




