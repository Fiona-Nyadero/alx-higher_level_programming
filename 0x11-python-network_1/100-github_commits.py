#!/usr/bin/python3
"""
Lists 10 most recent commits of a repository using GitHub API
"""
import requests
import sys


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/
            {owner_name}/{repository_name}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()

        commits = response.json()[:10]  # Get the 10 most recent commits

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
