#!/bin/bash
# Sends a JSON POST request and displays the response body
curl -sX POST -H "Content-Type: application/json" -d "$json_content" "$1"
