#!/usr/bin/python3
"""
Takes a letter, sends a POST request to search_user,
and displays the response
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': q}

    try:
        rspnse = requests.post(url, data=data)
        rspnse.raise_for_status()

        try:
            json_data = rspnse.json()

            if json_data:
                print("[{}] {}".format(json_data['id'], json_data['name']))
            else:
                print("No result")

        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
