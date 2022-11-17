#!/usr/bin/python3
import os
import argparse

parser = argparse.ArgumentParser(description='Produces a list to be used for the detection and anlysis of circRNA.')
parser.add_argument("-i", "--input", help="Absolute path to folder containing sample files. Example: /home/user/data/mouse/")
parser.add_argument("-p", "--prefix", help="Name of list file to create. Example: test_data.list")
parser.add_argument("-l", "--list", help="Absolute path to list if user wants to define samples. Examples /home/user/data/samples.list", default="none")
args = parser.parse_args()
path = args.input
prefix = args.prefix
list = args.list
if list == "none":
        dir = "Running listmaker on the following directory: " + path
        print(dir)
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
if list != "none":
        dir = "Running listmaker on the following directory: " + path
        print(dir)
        os.chdir(path)
        gtf = prefix + "_gtf.list"
        geneout = prefix + "_geneout.list"
        with open(list, 'r') as read_obj:
                sample_data = []
                for line in read_obj:
                        content_check = line.rstrip().split()
                        sample_data.append(content_check[0])
        with open(gtf, 'w') as write_obj:
                for R1path in next(os.walk('.'))[1]:
                        if R1path in sample_data:
                                write_obj.write(R1path)
                                write_obj.write("\t")
                                gtfpath = path + "/" + R1path + "/output/" + R1path + ".gtf"
                                write_obj.write(gtfpath)
                                write_obj.write("\n")
                write_obj.close()
        with open(geneout, 'w') as write_obj:
                for R1path in next(os.walk('.'))[1]:
                        if R1path in sample_data:
                                write_obj.write(R1path)
                                write_obj.write("\t")
                                geneoutpath = path + "/" + R1path + "/output/gene/" + R1path + "_out.gtf"
                                write_obj.write(geneoutpath)
                                write_obj.write("\n")
                write_obj.close()
        read_obj.close()
