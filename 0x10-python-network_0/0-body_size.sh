#!/bin/bash
# Displays the size of response body of a URL

# Check for a URL argument
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

curl -s "$1" | wc -c
