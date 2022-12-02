#!/usr/bin/python3
import os
import argparse

parser = argparse.ArgumentParser(description="Produces a list to be used for the detection and anlysis of circRNA.")
parser.add_argument("-i", "--input", help="Absolute path to input file to identify . Example: /path/input.fastq or /path/input.fasta or (input.fq/input.fa)")
parser.add_argument("-o", "--output", help="Absolute path to output file. Example: output_split.list")
parser.add_argument("-p", "--percentage", help="Percentage Identity to retain. Example 60% retains reads with under 60% of the chosen base option.")
parser.add_argument("-b", "--base", help="Nucleic Base to sort based off. C,T,G,A")
args = parser.parse_args()
input = args.input
output = args.output
percentage = args.percentage
base = args.base

#Check input extension
ext = os.path.splitext(input)[-1].lower()
perc = int(percentage) / 100
with open(input, 'r') as read_obj:
        if any(ext in fq_format for fq_format in (".fq", ".fastq")):
                print("fastq")
        elif any(ext in fa_format for fa_format in (".fa", ".fasta")):
                update = "Now splitting " + input + " by Nucleic Base " + base + " based off a percentage Identity of " + percentage + "%"
                print(update)
                with open(output, 'w') as write_obj:
                        for line in read_obj:
                                basecount = 0
                                line1 = line
                                line2 = next(read_obj)
                                split = list(line2)
                                length = len(split)
                                for character in split:
                                        if character == base:
                                                basecount = basecount + 1
                                if (int(basecount) / int(length)) < perc:
                                        write_obj.write(line1)
                                        write_obj.write(line2)
        else:
                print("Incorrect File Format Please View Manual For Usage.")
