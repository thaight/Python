#!/bin/python
import os
import numpy as np
import argparse

def count_starts(bed_file):
    max_coord = 0
    counts = []
    with open(bed_file, 'r') as f:
        for line in f:
            cols = line.strip().split('\t')
            start = int(cols[1])
            end = int(cols[2])
            strand = cols[5]
            max_coord = max(max_coord, end)  # Track the largest end coordinate
            if strand == '+':
                counts.append(start)
    return counts, max_coord

def process_directory(directory):
    bed_files = [f for f in os.listdir(directory) if f.endswith('.bed')]
    max_sequence_length = 0
    all_counts = []

    # Find the maximum sequence length and collect start counts
    for bed_file in bed_files:
        file_path = os.path.join(directory, bed_file)
        counts, file_max = count_starts(file_path)
        max_sequence_length = max(max_sequence_length, file_max)  # Update global max length
        all_counts.append(counts)

    # Initialize count matrix with detected sequence length
    counts_matrix = np.zeros((max_sequence_length, len(bed_files) + 1), dtype=int)
    counts_matrix[:, 0] = np.arange(1, max_sequence_length + 1)  # First column is base positions

    # Fill count matrix
    headers = ['Base_Position']
    for i, bed_file in enumerate(bed_files):
        for start in all_counts[i]:
            if start < max_sequence_length:
                counts_matrix[start, i + 1] += 1
        headers.append(bed_file.replace('.bed', ''))  # Add the file name to headers

    return counts_matrix, headers, max_sequence_length

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process bed files and generate CSV matrix.")
    parser.add_argument('-p', '--project', required=True, help="Project directory path where the output CSV will be saved")

    args = parser.parse_args()
    
    # Normalize the project path to remove any trailing slashes
    project_path = os.path.normpath(args.project)
    
    # Extract the project name from the normalized directory path
    project_name = os.path.basename(project_path).replace("_output", "")

    # Process the directory and determine sequence length automatically
    matrix, headers, sequence_length = process_directory(project_path)
    
    # Define the output CSV file path with the project name
    output_csv_path = os.path.join(project_path, f"{project_name}.csv")
    
    # Save the matrix to a CSV file
    np.savetxt(output_csv_path, matrix, fmt='%d', delimiter=',', header=','.join(headers), comments='')
    print(f"CSV file saved as '{output_csv_path}' with sequence length {sequence_length}")

if __name__ == "__main__":
    main()
