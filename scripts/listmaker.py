#!/usr/bin/python3
import os
import argparse

parser = argparse.ArgumentParser(description='Produces a list to be used for the detection and anlysis of circRNA.')
parser.add_argument("-i", "--input", help="Absolute path to folder containing sample files. Example: /home/user/data/mouse/")
parser.add_argument("-o", "--prefix", help="Name of list file to create. Example: test_data.list.")
args = parser.parse_args()
path = args.input
prefix = args.prefix
dir = "Running listmaker on the following directory: " + path
print(dir)
#Works on the current directory you are in
os.chdir(path)
output = prefix + ".list"
gtf = prefix + "_gtf.list"
geneout = prefix + "_geneout.list"
with open(output, 'w') as write_obj:
        for R1path in next(os.walk('.'))[1]:
                write_obj.write(R1path)
                write_obj.write("\n")
        write_obj.close()
with open(gtf, 'w') as write_obj:
        for R1path in next(os.walk('.'))[1]:
                write_obj.write(R1path)
                write_obj.write("\t")
                gtfpath = path + "/" + R1path + "/output/" + R1path + ".gtf"
                write_obj.write(gtfpath)
                write_obj.write("\n")
        write_obj.close()
with open(geneout, 'w') as write_obj:
        for R1path in next(os.walk('.'))[1]:
                write_obj.write(R1path)
                write_obj.write("\t")
                geneoutpath = path + "/" + R1path + "/output/gene/" + R1path + "_out.gtf"
                write_obj.write(geneoutpath)
                write_obj.write("\n")
        write_obj.close()
