#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me and receives "You got me!"
curl -s -L -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
