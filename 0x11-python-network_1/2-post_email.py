#!/usr/bin/python3
"""POST an email"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    emailData = {'email': sys.argv[2]}
    emailEncoded = urllib.parse.urlencode(emailData).encode('ascii')
    pyRequest = urllib.request.Request(sys.argv[1], emailEncoded)
    with urllib.request.urlopen(pyRequest) as httpResponse:
        dataDecoded = httpResponse.read().decode('utf-8')
        print(dataDecoded)
