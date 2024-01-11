#!/bin/bash
# Requests OPTIONS & displays allowed HTTP methods only
curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d ' ' -f 2-
