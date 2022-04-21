#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS https://google.com | grep allow | cut -d " " -f 2-
