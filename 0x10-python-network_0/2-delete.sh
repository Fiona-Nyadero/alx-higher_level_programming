#!/bin/bash
# Sends a DELETE request & displays the body of the response

# Check for a URL argument
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

delres=$(curl -sX DELETE "$1")
echo "$delres"

