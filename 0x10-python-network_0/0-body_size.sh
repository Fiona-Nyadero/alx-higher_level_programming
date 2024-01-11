#!/bin/bash
# Displays the size of response body of a URL
curl -s "$1" | wc -c
