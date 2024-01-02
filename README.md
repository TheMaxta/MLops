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
- If you encounter issues with port 5000 on a Mac (commonly blocked), you can specify a different port using: `mlflow server --host 0.0.0.0 --port 5001`
- If you encounter issues with port 5000 on a Mac (commonly blocked), you can specify a different port using: `mlflow ui --port 5001`
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



### Explanation of the PATH Export Command

The command `export PATH="/Users/maxmahlke/anaconda3/envs/myenv/bin:$PATH"` is used in Unix-like operating systems to modify the environment variable `PATH`. Here's a breakdown of what this command does:

- `export`: This is a shell builtin in Bash and other Unix shells. It is used to set environment variables and make them available to future subprocesses.

- `PATH`: `PATH` is an environment variable. It tells the shell where to look for executable files. When you type a command in the terminal, the shell searches the directories listed in your `PATH` in order to find an executable file with that name.

- `"/Users/maxmahlke/anaconda3/envs/myenv/bin:$PATH"`: This sets the new value of the `PATH` variable. It has two parts:
  - `/Users/maxmahlke/anaconda3/envs/myenv/bin`: This is the path to the `bin` directory of the `myenv` Conda environment. By placing this directory at the beginning of the `PATH`, it ensures that the executables in this directory (like Python) are used preferentially over other versions installed on the system.
  - `$PATH`: This is the existing content of the `PATH` variable. By appending it to the new directory path, it ensures that all previously available commands remain accessible.

In essence, this command prepends the specified directory (`/Users/maxmahlke/anaconda3/envs/myenv/bin`) to the existing `PATH`, giving priority to the executables in the specified Conda environment. This is particularly useful for ensuring that the Python version and any installed packages specific to the `myenv` environment are used in preference to those installed elsewhere on the system.
