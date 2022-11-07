import argparse
import os
from os import path
from subprocess import call
import sys

parser = argparse.ArgumentParser(description='Split fastq files into X files sized Y.')
parser.add_argument("-o", "--output", help="Absolute path to store new files")
parser.add_argument("-i", "--input", help="Absolute path to input file")
parser.add_argument("-p", "--prefix", help="prefix for file")
parser.add_argument("-n", "--length", help="number of reads per file",
                    default=1000000, type=int)
args = parser.parse_args()
output = args.output
input = args.input
prefix = args.prefix
length = args.length

def read_write():
    i = 0
    n = 0
    filename = output + prefix + '_' + str(n) + '.fastq'
    f = open(filename, 'w')
    print('Writing to ' + filename)
    try:
        with open(input, 'r') as sample_file:
            for line in sample_file:
                f.write(line)
                i += 1
                if i == args.length*4:
                    f.close()
                    n += 1
                    filename = path.join(output, prefix + '_' + str(n) + '.fastq')
                    i = 0
                    f = open(filename, 'w')
                    print('Writing to '+ filename)
    except EOFError:
        f.close()
    if i == 0:
        os.remove(filename)
        print('Removed empty file')
    print('Done')

read_write()
