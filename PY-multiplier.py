import os
import subprocess

listF = []

for i in listF:
    infile = "mission-parser.py"
    outfile = "10.txt"

    delete_list = ['***']
    number = i

    fin = open(infile)
    fout = open(outfile, "w+")

    for line in fin:
        for word in delete_list:
            line = line.replace(word, str(i))
            fout.write(line)
    fin.close()
    fout.close()
    os.rename('10.txt', str(i) + '.py')
