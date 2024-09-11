#!/bin/bash
# cURL a JSON file
curl -sH 'Content-Type: application/json' -d "$(cat "$2")" "$1"
