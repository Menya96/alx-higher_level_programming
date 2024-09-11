#!/usr/bin/python3
"""Using requests to fetch X-Request-Id value"""

if __name__ == '__main__':
    import requests
    import sys

    httpResponse = requests.get(sys.argv[1])
    print(httpResponse.headers.get('X-Request-Id'))
