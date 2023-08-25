#!/bin/python3
import argparse
'''
The following script takes as input an reference file, a start index, end index, and chromosome and returns the sequence for that given start:end.
Version: 1.0
Date: August 24th, 2023
Publisher: Travis Haight
'''
def read_file(seq_path, out_path, start, end, chrom):
    start_coord = int(start) -1 #Corrects 0 base system
    end_coord = int(end)
    data = ""
    pattern = ">" + chrom
    start_match = False
    with open(seq_path, 'r') as seq_file, open(out_path, 'a') as out_file:
        for line in seq_file:
            if line.strip() == pattern:
                start_match = True
                continue
            if start_match:
                if line.startswith(">"):
                    break
                else:
                    data += line.strip()
        max = len(data)
        if max <= end_coord:
            end = max
        if start_coord >= max:
            print("That chromosome is not that long please choose a new interval:")
            return()
        id = pattern + " " + str(start) + ":" + str(end) + '\n'
        out_file.write(id)
        out_file.write(data[start_coord:end_coord])
        out_file.write('\n')

parser = argparse.ArgumentParser(description='Grab the sequence of index start:end from a reference file for downstream use.')
parser.add_argument('-i', '--input', help='Absolute path to a file that you are grabbing the sequence from.')
parser.add_argument('-o', '--output', help='Absolute path to a output file.')
parser.add_argument('-s', '--start', help='Start Index that you are grabbing.')
parser.add_argument('-e', '--end', help='End Index that you are grabbing.')
parser.add_argument('-c', '--chrom', help='Chromosome to search. Example: chr7.')
args = parser.parse_args()
input = args.input
output = args.output
start = args.start
end = args.end
chrom = args.chrom
result = read_file(input, output, start, end, chrom)
