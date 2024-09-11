#!/usr/bin/python3
"""POST an email using requests module"""

if __name__ == '__main__':
    import requests
    import sys

    email = {'email': sys.argv[2]}
    httpResponse = requests.post(sys.argv[1], email)
    print(httpResponse.text)
