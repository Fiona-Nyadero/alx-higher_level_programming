#!/bin/bash
# Sends a GET request, with custom header and response body
curl -sH "X-School-User-Id: 98" "$1"
