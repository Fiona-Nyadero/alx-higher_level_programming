#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST
HTTP request & displays the response body
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print(content)
