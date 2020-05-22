#!/usr/bin/env python

'''Takes a set of pairs of values, first one mean, second one standard deviation and outputs a series of commands
to run PCR_dup_modeller on the dataset with those values.'''

import sys

length = len(sys.argv) - 1
print("#!/bin/bash")

if length % 2 == 0:
    x = 1
    pairs_dict = {}

    while x < length:
        mean = sys.argv[x]
        standard_deviation = sys.argv[x+1]

        statement = '''submit_pipeline_python ~/SHAREDBEN/Scripts/SpotDup -d./ --log=PCR_sfd_{}_{}.log --stdout=PCR_sfd_{}_{}.res -m{} -s{}'''
        finished_statement = statement.format(mean, standard_deviation, mean, standard_deviation, mean,
                                              standard_deviation)
        print(finished_statement)

        x += 2

else:
    print("Wrong number of arguments given. Arguments must be given in pairs.")
    sys.exit()
