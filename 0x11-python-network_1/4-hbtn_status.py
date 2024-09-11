#!/usr/bin/python3
"""Using requests module to fetch url data"""

if __name__ == '__main__':
    import requests

    httpResponse = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(httpResponse.text)}')
    print(f'\t- content: {httpResponse.text}')
