#!/bin/bash
# cURL only Method (Allow) 
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f 2-
