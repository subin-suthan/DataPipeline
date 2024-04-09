#!/bin/bash

# Define an array of subdirectories
subdirectories=("2014" "2015" "2016" "2017" "2018" "2019" "2020" "2021" "2022" "2023" "2024")

# Read patterns from random_station_id.txt
while IFS= read -r pattern; do
    # Loop over each subdirectory
    for subdir in "${subdirectories[@]}"; do
        # Use wget to download files matching the current pattern from each subdirectory
        wget -r -A "$pattern*" "ftp://ftp.ncdc.noaa.gov/pub/data/noaa/$subdir"
    done
done < random_station_id.txt

