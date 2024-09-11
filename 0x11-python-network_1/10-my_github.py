#!/usr/bin/python3
"""Using the GitHub API"""

if __name__ == '__main__':
    import requests
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    githubUrl = 'https://api.github.com/user'
    httpResponse = requests.get(githubUrl, auth=(user, passwd))
    print(httpResponse.json().get('id'))
