import requests
import os

github_token = os.environ.get('GITHUB_TOKEN')

url = 'https://api.github.com/repos/djigitlike/testrep-2/pulls?base=release'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer {github_token}'
}

resp = requests.get(url=url, headers=headers)
pull_requests = resp.json()

pr_dev_to_release_list = [pr for pr in pull_requests if pr['head']['ref'] == 'dev']

# pre_release has been created by someone
if pr_dev_to_release_list.length > 1:
    exit(1)
