#!/usr/bin/python3
"""Fetching URL data & displaying X-Request-Id"""

if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as httpResponse:
        allHeadersDict = httpResponse.info()
        for headr in allHeadersDict:
            if headr == 'X-Request-Id':
                print(allHeadersDict[headr])
