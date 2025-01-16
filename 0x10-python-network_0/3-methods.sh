#!/bin/bash
# Displays all the HTTP methods the server will accept for the URL
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-
