#!/bin/bash
# Sends a JSON POST request and displays the response body
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
