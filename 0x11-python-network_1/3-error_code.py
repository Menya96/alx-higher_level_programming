#!/usr/bin/python3
"""Handling URL exceptions and errors"""

if __name__ == '__main__':
    import urllib.request
    import sys

    argUrl = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(argUrl) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')
