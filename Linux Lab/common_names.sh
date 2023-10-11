#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 file1 file2"
    exit 1
fi

file1=$1
file2=$2

if [ ! -f "$file1" ] || [ ! -f "$file2" ]; then
    echo "Error: Both files should exist."
    exit 1
fi

sort "$file1" -o "$file1"
sort "$file2" -o "$file2"

common_names=$(comm -12 "$file1" "$file2")

if [ -n "$common_names" ]; then
    echo "Common names found in both files:"
    echo "$common_names"
else
    echo "No common names found in both files."
fi