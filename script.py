import requests
import os

github_token = os.environ.get('GITHUB_TOKEN')

url = 'https://api.github.com/repos/djigitlike/testrep-2/pulls?base=release'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer {github_token}'
}

resp = requests.get(url=url, headers=headers)
data = resp.json()

exit(1)
