#!/usr/bin/python3
"""
Takes a URL, sends a HTTP request &
Displays the response body
Prints an error message if HTTP statuscode >= 400
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        rspnse = requests.get(url)
        rspnse.raise_for_status()

        print(rspnse.text)

    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
