import requests

request = requests.post(f"http://localhost:5005/alerts")
print(request.status_code)