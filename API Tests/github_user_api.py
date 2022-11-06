import requests
import json
from pathlib import Path

# Call API
target = input('Username of the user you are looking for >_ ')
url = f"https://api.github.com/users/{target}"

# Status codes are great to know
r = requests.get(url)
print(f"Code: {r.status_code} - Reason: {r.reason}")

# Format response into json dictionary
response = r.json()
print(response)
