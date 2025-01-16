#!/bin/bash
# Sends a JSON POST request to a URL with the content of a file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
