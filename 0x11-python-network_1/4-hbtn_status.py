#!/usr/bin/python3
""" Fetches url/status using requests """
import requests


url = "https://alx-intranet.hbtn.io/status"

try:
    respnse = requests.get(url)
    respnse.raise_for_status()
    utf8_cntnt = respnse.text

    print("Body response:")
    print("\t- type:", type(respnse.text))
    print("\t- content:", utf8_cntnt)

except requests.exceptions.RequestException as e:
    print("Error:", e)
