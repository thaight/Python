#!/bin/python3
'''
The following script takes as input a gff3 file and converts it to gtf format
Version: 1.0
Date: August 10th, 2023
Publisher: Travis Haight
'''
def convert_gff3_to_gtf(gff3_file):
    ''' This functions takes as input a gff3 file and converts it to gtf format for downstream analysis '''
    gtf_file = gff3_file.replace(".gff3", ".gtf")
    with open(gff3_file, 'r') as gff, open(gtf_file, 'w') as gtf:
        for line in gff:
            if line.startswith('#'):
                #Comments allowable in gff3 but not gtf files
                continue
            fields = line.strip().split('\t')
            if len(fields) != 9:
                #This checks each line containes 9 elements and skips if missing information
                continue
            seqname, source, feature, start, end, score, strand, frame, attributes = fields
            #Create the GTF line
            gtf_line = '\t'.join([seqname, source, feature, start, end, score, strand, frame])
            # Extract the attributes and convert to GTF format
            attribute_pairs = [pair.split('=') if '=' in pair else (pair, '') for pair in attributes.split(';')]
            gtf_attributes = ' '.join(['{} "{}"'.format(key, value) for key, value in attribute_pairs])
            gtf_line += ' ' + gtf_attributes + '\n'
            gtf.write(gtf_line)

#Main Usage
parser = argparse.ArgumentParser(description='Pipeline for the conversion of gff3 to gtf format..')
parser.add_argument('-i', '--input', help='Absolute path to gff3 file. /home/test/test1.gff3')
args = parser.parse_args()
input = args.input
convert_gff3_to_gtf(input)
