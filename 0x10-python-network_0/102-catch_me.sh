#!/bin/bash
# Sends request to catch_me website endpoint with specific behavior
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
