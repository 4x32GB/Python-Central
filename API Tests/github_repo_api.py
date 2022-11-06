import requests
import json

# Make API call and check the response
query_selector = "?q=language:python+sort:stars+stars:>10000"
repo_url = f"https://api.github.com/search/repositories{query_selector}"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(repo_url, headers=headers)
# print(f"Code: {r.status_code} - Reason: {r.reason}")

# Convert response to a dictionary 
response = r.json()

print(f"Total repositories: {response['total_count']}")
print(f"Complete results: {not response['incomplete_results']}")

# Explore information about the repositories
repo_dicts = response['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine first repository
repo_dicts = repo_dicts[0]
print(f"\nKeys: {len(repo_dicts)}")
for key in sorted(repo_dicts.keys()):
    print(key)