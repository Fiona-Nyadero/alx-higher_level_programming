#!/bin/bash
# Sends POST request (specified parameters) & displays the response body

# Check for URL argument
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

email="test@gmail.com"
subject="I will always be here for PLD"
post_resp=$(curl -sX POST -d "email=$email&subject=$subject" "$1")
echo "$post_resp"
