#!/usr/bin/python3
"""
Takes a URL, sends a HTTP request,
& displays the X-Request-Id val in the res header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        rspnse = requests.get(url)
        rspnse.raise_for_status()

        print(rspnse.headers.get('X-Request-Id'))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
