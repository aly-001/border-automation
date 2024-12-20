#!/bin/bash

# Ensure the output directory exists
mkdir -p split_chapters_txt

# Loop through each PDF and convert
for pdf in chapter_*.pdf; do
    base_name=$(basename "$pdf" .pdf)
    pdftotext "$pdf" "split_chapters_txt/${base_name}.txt"
done

