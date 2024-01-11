#!/usr/bin/python3
"""
Takes a URL, sends a HTTP  request,& displays the response body
Handling urllib.error.HTTPError exceptions
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print((response.read().decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
