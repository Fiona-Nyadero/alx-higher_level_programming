#!/bin/bash
# Sends a GET request, with custom header and response body

# Check for a URL argument
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

resbody=$(curl -sH "X-School-User-Id: 98" "$1")
echo "$resbody"
