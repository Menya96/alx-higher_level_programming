#!/usr/bin/python3
"""Fetching URL data using urllib module"""
if __name__ == '__main__':
    import urllib.request

    alxUrl = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(alxUrl) as httpResponse:
        responseData = httpResponse.read()

        print('Body response:')
        print(f'\t- type: {type(responseData)}')
        print(f'\t- content: {repr(responseData)}')
        print(f'\t- utf8 content: {responseData.decode("utf-8")}')
