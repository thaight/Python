#!/bin/python3
#Version 1.0
#Author: Travis Haight

#Imports
import argparse

def process_and_insert_lines(line1, line2, count):
    col1 = line1.split(',')
    col2 = line2.split(',')
    transcript1 = col1[0] + "." + col1[1] #Rename transcript1 to include the full identification (i.e. transcript1.1)
    transcript2 = col2[0]+  "." + col2[1] #Rename transcript2 to include the full identification (i.e transcript2.1)
    ID = "Gap_" + transcript1 + "_" + transcript2 #New gap sequence name that will insert between transcript1/2
    start = int(col1[4]) + 1 #Calculate gap start position based off transcript1 end
    end = int(col2[3]) - 1 #Calculate gap end position based off transcript2 start
    length = end - start #Calculate the length of the gap position
    ensemble = "NA" #This gap sequence wont have  an associated ensemble so we will define as NA here
    #Calculate new line counts
    transcript1_count = count + 1
    newtranscript_count = count + 2
    #Define new line content and reformated transcript1 line content
    new_transcript1 = transcript1 + "," + str(transcript1_count) + "," + col1[3]+ "," + col1[4] + "," + col1[5] + "," + col1[6].strip()
    new_content = ID + "," + str(newtranscript_count) + "," + str(start) + "," + str(end) + "," + str(length) + "," + ensemble
    return new_content, new_transcript1, newtranscript_count

#Argument Import
parser = argparse.ArgumentParser(description='Takes as input a .csv file with 7 columns and adds the gap coordinates between each candidat>
parser.add_argument('-i', '--input', help='Absolute path to a input .csv file')
parser.add_argument('-o', '--output', help='Absolute path to a output .csv file.')
args = parser.parse_args()
input_file = args.input
output_file = args.output

#Usage Starts
with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    lines = input_csv.readlines()
    #Reformat header to match new pattern
    header =  lines[0]
    col3 = header.split(',')
    new_header = col3[0] + "," + col3[1] + "," + col3[3] + "," + col3[4] + "," + col3[5] + "," + col3[6].strip()
    output_csv.write(new_header + '\n')
    count = 0
    for i in range(1, len(lines) - 1): #Loop through lines but account for  the first line (The header) being handled above
        line1 = lines[i]
        line2 = lines[i + 1]
        new_content, new_line1, count  = process_and_insert_lines(line1, line2, count)
        #Write out the reformated lines
        output_csv.write(new_line1 + '\n')
        output_csv.write(new_content + '\n')
        #Handle the last line in the file
        if i == len(lines) - 2:
            col = line2.split(',')
            final_transcript = col[0] + "." + col[1]
            new_final_content = final_transcript + "," + str(count + 1) + "," + col[3]+ "," + col[4] + "," + col[5] + "," + col[6].strip()
            output_csv.write(new_final_content)
