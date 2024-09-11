#!/usr/bin/python3
"""Search API (JSON): using requests post"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) == 1:
        q = ''
    else:
        q = sys.argv[1]
    qData = {'q': q}
    serverUrl = 'http://0.0.0.0:5000/search_user'
    httpResponse = requests.post(serverUrl, data=qData)
    try:
        outpt = httpResponse.json()
        if outpt == {}:
            print('No result')
        else:
            print(f'[{outpt.get("id")}] {outpt.get("name")}')
    except ValueError:
        print('Not a valid JSON')
