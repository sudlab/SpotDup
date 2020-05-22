'''Computes a fragment length distibution and outputs it in the same format
as salmon's flendist.txt.

Will only used non-multimapped reads

Usage:

python flendist.py BAMFILE

distribution comes on stdout. Note that it will be mixed with the log unless
you redirect one of log (using -L) or stdout (using -S). 



'''
from cgatcore import experiment as E
from collections import defaultdict
import pysam

parser = E.OptionParser(usage = globals()["__doc__"])
options, args = E.start(parser)

bamfile = pysam.AlignmentFile(args[0])

lengthdist = [0.0]*1001
total = 0
all_total = 0
E.info("Starting Run")
for read in bamfile.fetch(until_eof=True):
    all_total += 1

    if all_total %1000000 == 0:
        E.debug("Done %s reads; %s used" % (all_total, total))

    if read.is_unmapped:
        continue
    
    if read.has_tag("NH") and read.get_tag("NH") != 1:
        continue

    if read.is_read2:
        continue

    flen = read.template_length

    total += 1
    
    if abs(flen) <= 1000:
        lengthdist[abs(flen)] += 1.0


bamfile.close()

lengthdist = [f/total for f in lengthdist]

options.stdout.write("\t".join(map(str,lengthdist)))
E.info("Used %s reads out of %s to built distribution. Total weight = %s " % (total, all_total, sum(lengthdist)))
E.stop()


