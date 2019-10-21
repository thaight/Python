
import os
import commands
import sys
import getopt

def filter_by_len(ifile,seq_len,ofile):
    c=0
    list=[]
    f=open(ofile,'w')
    for line in file(ifile):
        c+=1
        #print c
        list.append(line.strip())
        if c==4:
            #print len(list[1])
            if len(list[1])==int(seq_len):
                [f.write('%s\n'%j) for j in list]
            c=0
            list=[]
    f.close()
    #print 'Done'

def main(argv):
    ifile = ''
    ofile = ''
    seq_len=0
    try:
        opts, args = getopt.getopt(argv,"h:i:l:o:",["help","ifile=","seq_len=","ofile="])
        if not opts:
            print 'No options supplied'
            print 'Filter_fastq_by_Sequence_length.py -i <inputfile> -l <seq_length> -o <outputfile>'
            sys.exit(2)
    except getopt.GetoptError:
        print 'Usage:'
        print 'Filter_fastq_by_Sequence_length.py -i <inputfile> -l <seq_length> -o <outputfile>'
        sys.exit(2)
    #print opts
    #print args
    for opt, arg in opts:
        if opt in ('-h',"--help"):
            print 'Usage:'
            print 'Filter_fastq_by_Sequence_length.py -i <inputfile> -l <seq_length> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            ifile = arg
        elif opt in ("-o", "--ofile"):
            ofile = arg
        elif opt in ("-l", "--seq_length"):
            seq_len = arg

    print 'Using Following inputs'
    print 'Input file is ', ifile
    print 'Seq_length is ', seq_len
    print 'Output file is ', ofile
    print 'Filtering in Progress......'

    return (ifile,seq_len,ofile)

if __name__ == "__main__":
    param=main(sys.argv[1:])
    filter_by_len(param[0],param[1],param[2])
    print 'Done'
