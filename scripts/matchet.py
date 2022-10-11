#!/usr/bin/env python3
age_file = "/home/travis/Desktop/GSE12597/circ_edits/rtg4510_2month"
match_file = "/home/travis/Desktop/GSE125957/rtg4510_all_DE.tsv"



file_name = "/home/travis/Desktop/GSE125957/temp.sam"
temp_file = "/home/travis/Desktop/GSE125957/SRR8512303_matches.txt"
match_file = "/home/travis/Desktop/GSE125957/rtg4510_all_DE.tsv"





with open(file_name, 'r') as read_obj1, open(match_file, 'r') as read_obj2, open(temp_file, 'w') as write_obj:
    next(read_obj2) #Stores header information for later use
    for line2 in read_obj2:
         X = (line2.split('\t')[1])
         for line1 in read_obj1:
             if X in line1:
                 #Info contains the circRNA information from the pipeline including age/regulation
                 info = line2.split('\t')[0] + ":" + line2.split('\t')[1] + "|" + line2.split('\t')[2] + "|" + (line2.split('\t')[6]).rstrip() + "|" + line2.split('\t')[5] + "\n"
                 #Header contains the read circRNA information concatanated with the info
                 header = line1.split('\t')[0] + "\t" + line1.split('\t')[1] + "\t" + line1.split('\t')[2] + "\t" + line1.split('\t')[3] + "\t" + info
                 #Writes out header information to new file
                 write_obj.write(header)
                 #Writes out read to new file
                 write_obj.write(line1.split('\t')[9])

