#!/bin/bash
# Sends a POST request with specific parameters and shows response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
