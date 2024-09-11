#!/usr/bin/python3
"""requests module: Handling URL exceptions and errors"""

if __name__ == '__main__':
    import requests
    import sys

    httpResponse = requests.get(sys.argv[1])
    if httpResponse.status_code >= 400:
        print(f'Error code: {httpResponse.status_code}')
    else:
        print(httpResponse.text)
