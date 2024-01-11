#!/bin/bash
# Displays only the response status code of a URL request
curl -so /dev/null -w "%{http_code}" "$1"
