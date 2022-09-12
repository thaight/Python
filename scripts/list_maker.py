import os

#Works on the current directory you are in
with open('sample.list', 'w') as write_obj:
        for R1path in next(os.walk('.'))[1]:
                write_obj.write(R1path)
                write_obj.write("\n")
        write_obj.close()
