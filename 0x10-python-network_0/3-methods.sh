#!/bin/bash
# Requests OPTIONS & displays allowed HTTP methods only

# Check for URL argument
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

HTallow_methods=$(curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d ' ' -f 2-)
echo "$HTallow_methods"
