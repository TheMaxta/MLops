import mlflow
import mlflow.sklearn


# Set the tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5001")


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

with mlflow.start_run():
    # Load the Iris dataset
    data = load_iris()
    X = data.data
    y = data.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    n_estimators = 50

    # Create and train a RandomForestClassifier
    clf = RandomForestClassifier(n_estimators)
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Log metrics
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)

    # Log parameters
    mlflow.log_params({"n_estimators": n_estimators, "random_state": 45})

    # Log the model as an artifact
    mlflow.sklearn.log_model(clf, "model")


best_run = mlflow.search_runs(order_by=["metrics.accuracy desc"]).iloc[0]
best_run_id = best_run.run_id
best_model = mlflow.sklearn.load_model("runs:/" + best_run_id + "/model")

