import requests
import os

github_token = os.environ.get('GITHUB_BOT_TOKEN')

url = 'https://api.github.com/repos/djigitlike/testrep-2/pulls?base=release'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer {}'.format(github_token)
}

print('Sending request to get all open pull request into release ...')
resp = requests.get(url=url, headers=headers)

if resp.status_code != 200:
    print('Request failed. Status: {}. Reason: {}'.format(rest.status_code, resp.content))
    exit(1)
    

pull_requests = resp.json()

pr_dev_to_release_list = [pr for pr in pull_requests if pr['head']['ref'] == 'dev']

# pre_release has been already created before
if len(pr_dev_to_release_list) > 0:
    print('Pull request from dev into release exists. Can not create a new pull request into dev!')
    exit(1)

print('Success')
