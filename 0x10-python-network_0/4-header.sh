#!/bin/bash
# Sends a GET request to the URL with a custom header and displays response
curl -sH "X-School-User-Id: 98" "$1"
