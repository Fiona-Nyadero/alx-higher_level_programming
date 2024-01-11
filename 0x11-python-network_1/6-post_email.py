#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request, and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    try:
        rspnse = requests.post(url, data=data)
        rspnse.raise_for_status()

        print("Your email is:", rspnse.text)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
