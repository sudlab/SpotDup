#!/usr/bin/env python

from cgat import FastaIterator
from cgatcore import iotools
import re
from sys import argv

###Define files
input_fasta = argv[1]

### Open files as fasta files
infile = iotools.open_file(input_fasta, "r")

oneA=0
oneG=0
oneT=0
oneC=0
oneO=0

twoA=0
twoG=0
twoT=0
twoC=0
twoO=0

thrA=0
thrG=0
thrT=0
thrC=0
thrO=0

i=0

###Iterate over and change titles if they are matched.
for transcript in FastaIterator.iterate(infile):
    if transcript.sequence[0] == "A":
        oneA+=1
    elif transcript.sequence[0] == "G":
        oneG+=1
    elif transcript.sequence[0] == "T":
        oneT+=1
    elif transcript.sequence[0] == "C":
        oneC+=1
    else:
        oneO+=1
        
    if transcript.sequence[1] == "A":
        twoA+=1
    elif transcript.sequence[1] == "G":
        twoG+=1
    elif transcript.sequence[1] == "T":
        twoT+=1
    elif transcript.sequence[1] == "C":
        twoC+=1
    else:
        twoO+=1
        
    if transcript.sequence[2] == "A":
        thrA+=1
    elif transcript.sequence[2] == "G":
        thrG+=1
    elif transcript.sequence[2] == "T":
        thrT+=1
    elif transcript.sequence[2] == "C":
        thrC+=1
    else:
        thrO+=1
    i+=1

print("Counts")    
print("Position\tA\tG\tT\tC")
print("1\t" + str(oneA) + "\t" + str(oneG) + "\t" + str(oneT) + "\t" + str(oneC))
print("2\t" + str(twoA) + "\t" + str(twoG) + "\t" + str(twoT) + "\t" + str(twoC))
print("3\t" + str(thrA) + "\t" + str(thrG) + "\t" + str(thrT) + "\t" + str(thrC))

print("Number of Transcripts Processed:", i)
peroneA=str((oneA/i)*100)
peroneG=str((oneG/i)*100)
peroneT=str((oneT/i)*100)
peroneC=str((oneC/i)*100)
pertwoA=str((twoA/i)*100)
pertwoG=str((twoG/i)*100)
pertwoT=str((twoT/i)*100)
pertwoC=str((twoC/i)*100)
perthrA=str((thrA/i)*100)
perthrG=str((thrG/i)*100)
perthrT=str((thrT/i)*100)
perthrC=str((thrC/i)*100)


print("")
print("Percentages")
print("Position\tA\tG\tT\tC")
print("1\t" + peroneA + "\t" + peroneG + "\t" + peroneT + "\t" + peroneC)
print("2\t" + pertwoA + "\t" + pertwoG + "\t" + pertwoT + "\t" + pertwoC)
print("3\t" + perthrA + "\t" + perthrG + "\t" + perthrT + "\t" + perthrC)
