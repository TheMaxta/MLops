# ===========================
# Command to execute script locally: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# Command to run Docker image: docker run -d -p 8000:8000 <fastapi-app-name>:latest


# Importing necessary libraries
from fastapi import FastAPI  # FastAPI framework for building APIs
from pydantic import BaseModel  # Pydantic for data validation and settings management
import mlflow  # MLflow for managing the machine learning lifecycle
import mlflow.sklearn  # MLflow's integration with scikit-learn
from mlflow.tracking import MlflowClient

# Creating an instance of the FastAPI app
app = FastAPI()

# Defining a Pydantic model for input data validation
class InputData(BaseModel):
    feature1: float  # Expected type of feature1
    feature2: float  # Expected type of feature2
    feature3: float  # Expected type of feature3
    feature4: float  # Expected type of feature4

# MLflow run ID for the best model
best_run_id = "5fe4bb83c40f48ae9b0334f64bc356fd"

# Setting the MLflow tracking URI to monitor and log experiments
mlflow.set_tracking_uri("http://127.0.0.1:5001")

# Loading the model from MLflow using the run ID
model = mlflow.sklearn.load_model("runs:/" + best_run_id + "/model")


@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API for IRIS dataset"}


# Defining a route for predictions
@app.post("/predict/")
async def predict(input_data: InputData):
    # Extract input features from the request
    features = [input_data.feature1, input_data.feature2, input_data.feature3, input_data.feature4]

    # Make predictions using the loaded model
    prediction = model.predict([features])[0]

    # Convert numpy data types to native Python data types for JSON serialization
    prediction = prediction.item()  # This will convert numpy.int64 to int

    # Create a response dictionary containing the prediction
    response_data = {"prediction": prediction}

    return response_data
