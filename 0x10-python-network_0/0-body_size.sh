#!/bin/bash
# Displays the size of response body of a URL

# Check for a URL argument
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URLbody_sz=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')
echo "$URLbody_sz"
