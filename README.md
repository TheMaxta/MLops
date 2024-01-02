# ML Ops Deployment and Model Training Roadmap

Welcome to the ML Ops Deployment and Model Training Roadmap! This guide is designed to provide a comprehensive understanding of the technologies and steps involved in deploying machine learning models. It's structured to help both beginners and experienced practitioners navigate the complexities of ML Ops.

## Overview
This roadmap outlines the necessary tools and technologies for effective machine learning model deployment, including TensorFlow, Pandas, Numpy, Scikit Learn for model building, ML Flow and W&B for model analysis, and Docker and Kubernetes for deployment. Fast API and Streamlit are also covered for creating APIs and web interfaces, respectively.

## Technologies:
### General ML Packages:
- **TensorFlow**: An end-to-end open-source platform for machine learning.
- **Pandas**: A fast, powerful, flexible, and easy-to-use data manipulation tool.
- **Numpy**: A fundamental package for scientific computing with Python.
- **Scikit Learn**: Simple and efficient tools for predictive data analysis.

### Model Analysis Packages:
- **ML Flow**: An open-source platform for managing the end-to-end machine learning lifecycle.
- **W&B (Weights & Biases)**: Tools for tracking experiments, versioning datasets, and project collaboration.

### Deployment:
- **Docker**: A set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.
- **Kubernetes**: An open-source system for automating deployment, scaling, and management of containerized applications.

### Fast API:
- An API framework for building APIs with Python 3.7+ based on standard Python type hints.

### Stream Lit:
- A framework for turning data scripts into shareable web apps.

## Next Steps:
Expand this guide into a comprehensive explanation of how to use these technologies mentioned. The purpose of this is to be a guide I can use to classify all of this information so that I may deploy models whenever necessary.

## Implementation Steps:
1. **Model Implementation**: Implement a basic random forest classifier using Fast API for backend API development.
2. **Web Interface**: Develop a Streamlit application to run inferences on the random forest model.
3. **Containerization**: Containerize the application using Docker for consistent deployment.
4. **Orchestration**: Use Kubernetes to manage and scale the Docker containers.

## Core Commands and Explanations:
### MLflow:
- To start the MLflow server, open a terminal tab and run: `mlflow ui`
- Note: Keep the MLflow server running while executing MLflow commands in a separate tab.
- If you encounter issues with port 5000 on a Mac (commonly blocked), you can specify a different port using: `mlflow ui --port <port_number>`
- While the MLflow server is running, execute your MLflow-integrated Python script in another terminal tab to log and track experiments.

### Streamlit:
- To run a Streamlit application, use: `streamlit run app.py`
- Ensure the necessary dependencies and the app script are properly set up before executing this command.

### Docker:
- Build a Docker image with: `docker build -t <image_name> .`
- Run the built Docker container using: `docker run <image_name>`
- Make sure Docker is installed and running on your system to execute these commands.

### Kubernetes:
- Create a deployment using a YAML file with: `kubectl apply -f <deployment_file>.yaml`
- View your deployments with: `kubectl get deployments`
- Ensure Kubernetes is configured correctly in your environment before using these commands.

## Notes:
These are big steps and big tasks so breaking them up into smaller goals is smart. Understanding that all of this is a very complicated and time-consuming effort is essential.

I will likely be spending the majority of the next couple of days working with Kubernetes and Docker because these are complicated and expansive technologies that will be ever-present in the coming years of my career. This will be time well spent.

