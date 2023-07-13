#!/bin/python3
import argparse

def file_comment_append(file_path):
    ''' This function reads in a file and saves all lines that do not start with # under the lines array for further downstream use '''
    ''' Note that you can edit search_param to match any symbol '''
    lines = []
    search_param = "#"
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            line = line.strip()
            if not line.startswith(search_param):
                lines.append(line)
        return lines

def content_grabber(candidate_list, end5, end3, chrom, out, sequence):
    ''' This function takes all circRNA candidates and based off a user defined interval (Start/End) grabs all circRNA within that interval and writes them out to a new file '''
    output_file = out
    sequence_file = sequence
    with open(output_file, 'w') as outfile, open(sequence_file, 'r') as seqfile:
        lines = seqfile.readlines()
        #Note that these file headers can be adjusted but it might break further steps
        outfile.write("Start_Coord\t")
        outfile.write("End_Coord\t")
        outfile.write("Junction_Read_ID\t")
        #outfile.write("Raw_Read\t")
        outfile.write("5'end of Back-Splice-Junction\t")
        outfile.write("3'end of Back-Splice-Junction\t")
        outfile.write("Back-Splice-Junction\n")
        for candidate in candidate_list:
            split = candidate.split()
            start = int(split[2])
            end = int(split[3])
            cand_chrom = split[1]
            read_ID = split[11]
            first_ID = read_ID.split(',')[0]
            #First verify that you are only searching the correct chromosome
            if cand_chrom == chrom:
                #Second verify that you are within the specified range
                if start >= end5 and end <= end3:
                    pattern = chrom + ":" + str(start) + "|" + str(end)
                    for i, line in enumerate(lines):
                        if pattern in line:
                            sequence_line = lines[i + 1]
                            sequence_5end = sequence_line[:25]
                            #Without this offset results in a new line as the last character
                            sequence_3end = sequence_line[-26:-1]
                            bsj_5end = sequence_line[:2]
                            #Without this offset results in a new line as the last character
                            bsj_3end = sequence_line[-3:-1]
                            backsplice_seq = bsj_3end + "|" + bsj_5end
                    outfile.write(str(start))
                    outfile.write("\t")
                    outfile.write(str(end))
                    outfile.write("\t")
                    outfile.write(first_ID)
                    outfile.write("\t")
                    outfile.write(sequence_5end)
                    outfile.write("\t")
                    outfile.write(sequence_3end)
                    outfile.write("\t")
                    outfile.write(backsplice_seq)
                    outfile.write("\n")

#Arguments parsed from user
parser = argparse.ArgumentParser(description='Produces a tab delimited output file that contains all circRNA hits within a interval.')
parser.add_argument("-i", "--input", help="Absolute path to input file. Currently accepts .ciri files as input")
parser.add_argument("-s", "--sequence", help="Absolute path to sequence file. Currently accepts index.fa files as input")
parser.add_argument("-o", "--output", help="Absolute path to output file. Currently produces a tab delimited file")
parser.add_argument("-c", "--chrom", help= "Chromosome to search interval on. Currently requires the formating of chr followed by the number (chr7)")
parser.add_argument("-s", "--start", help="Start of interval. For example 58957672")
parser.add_argument("-e", "--end", help="End of interval. For example 59625507")
args = parser.parse_args()
input_file = args.input
sequence_file = args.sequence
output_file = args.output
chrom = args.chrom
start = args.start
end = args.end

#Original testing paramaters        
#input_file = "/home/mobaxterm/Desktop/projects/DJ180913_R3/2-3.ciri"
#sequence_file = "/home/mobaxterm/Desktop/projects/DJ180913_R3/2-3_index.fa"
#output_file = "/home/mobaxterm/Desktop/projects/DJ180913_R3/2-3_snhg14.bed"
#Potential add function that pulls raw read from fastq file as well
#chrom = "chr7"
#start = 58957672
#end = 59625507
cand_list = file_comment_append(input_file)
content_grabber(cand_list, start, end, chrom, output_file, sequence_file)
