#!/usr/bin/python3
""" Fetches url/status using urllib """
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    cntent = response.read()
    utf8_cntent = cntent.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(cntent))
    print("\t- content:", cntent)
    print("\t- utf8 content:", utf8_cntent)
