#!/bin/bash
# Sends a GET request and displays body of a 200 status code response

# Check for URL argument
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

stat200_cdres=$(curl -sL -w "%{http_code}" "$1" -o /dev/null)
if [ "$stat200_cdres" -eq 200 ]; then
	    curl -sL "$1"
fi
