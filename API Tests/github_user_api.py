import requests
import json

# Make API call and check the response
target = input('GitHub Username: >_ ')
url = f"https://api.github.com/users/{target}"

r = requests.get(url)
print(f"Code: {r.status_code} - Reason: {r.reason}")

# Format response into json dictionary
response = r.json()
print(response)

# Process results
print(response.keys())