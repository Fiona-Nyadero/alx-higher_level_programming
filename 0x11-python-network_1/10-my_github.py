#!/usr/bin/python3
"""
Uses the GitHub API to display the user id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        rspnse = requests.get(url, auth=(username, token))
        rspnse.raise_for_status()

        json_data = rspnse.json()
        user_id = json_data.get('id')

        print(user_id)

    except requests.exceptions.RequestException as e:
        print("None")
