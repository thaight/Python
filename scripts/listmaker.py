#!/usr/bin/python3
import os
import argparse

parser = argparse.ArgumentParser(description='Produces a list to be used for the detection and anlysis of circRNA.')
parser.add_argument("-p", "--path", help="Absolute path to folder containing sample files. Example: /home/user/data/mouse/")
parser.add_argument("-o", "--output", help="Name of list file to create. Example: test_data.list.")
args = parser.parse_args()
path = args.path
output =args.output

dir = "Running listmaker on the following directory: " + path
print(dir)

#Works on the current directory you are in
with open(output, 'w') as write_obj:
        os.chdir(path)
        for R1path in next(os.walk('.'))[1]:
                write_obj.write(R1path)
                write_obj.write("\n")
        write_obj.close()
