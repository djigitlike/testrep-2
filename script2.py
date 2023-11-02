import requests
import os
import time
import json

github_token = os.environ.get('GITHUB_TOKEN')

url = 'https://api.github.com/repos/djigitlike/testrep-2/pulls?base=dev'
headers = {
    'Accept': 'application/vnd.github+json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(github_token)
}

print('Sending request to get open pull request...')
resp = requests.get(url=url, headers=headers)
print('Response received. Status code:  {}'.format(resp.status_code))

pull_requests = resp.json()

for pr in pull_requests:
    pr_url = pr.get('url')
    pr_id = pr_url.split('/')[-1]
    
    # trigger status checking for open PRs into dev
    r1 = requests.patch(url=pr_url, data=json.dumps({'state':'closed'}), headers=headers)
    
    if r1.status_code != 200:
        print('Pull request with id = {} was not closed. Reason: '.format(pr_id, r2.content))
    else:
        print('Pull request with id = {} was closed.'.format(pr_id))

    time.sleep(3) # 3 secs

    r2 = requests.patch(url=pr_url, data=json.dumps({'state':'open'}), headers=headers)

    if r2.status_code != 200:
        print('Pull request with id = {} was not reopened. Reason: {}'.format(pr_id, r2.content))
    else:
        print('Pull request with id = {} was reopened.'.format(pr_id))

print('Updating finished.')
