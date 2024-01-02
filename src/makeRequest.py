import requests

url = "http://localhost:8000/predict/"
data = {
    "feature1": 5.1,
    "feature2": 3.5,
    "feature3": 1.4,
    "feature4": 0.2
}

response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

if response.status_code == 200:
    print(response.json())
else:
    print("Failed to get a valid response")
