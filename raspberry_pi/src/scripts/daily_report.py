import requests

request = requests.post(f"http://localhost:5005/reports")
print(request.status_code)