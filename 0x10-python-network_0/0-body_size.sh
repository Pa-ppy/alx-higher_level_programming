#!/bin/bash
# It sends a request to the URL and displays the size of the response in bytes
curl -s "$1" | wc -c
