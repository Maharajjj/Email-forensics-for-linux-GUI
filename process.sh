#!/bin/bash

# Get the input and output folder paths from command-line arguments
input_folder="$1"
output_folder="$2"

# Verify that the input folder exists
if [ ! -d "$input_folder" ]; then
    echo "Input folder not found."
    exit 1
fi

# Verify that the output folder exists or create it if not
if [ ! -d "$output_folder" ]; then
    mkdir -p "$output_folder"
fi

# Process each .msg and .eml file in the input folder
for file in "$input_folder"/*.msg "$input_folder"/*.eml; do
    if [ -f "$file" ]; then
        # Run the Python script and capture its output
        response=$(python3 kanishkminiproject.py "$file") # Replace 'your_script.py' with your Python script
        
        # Create a response file with the same name as the input file
        response_file="$output_folder/$(basename "$file").response.txt"
        echo "$response" > "$response_file"
        echo "Processed $file and saved response as $response_file"
    fi
done

echo "Processing complete."
