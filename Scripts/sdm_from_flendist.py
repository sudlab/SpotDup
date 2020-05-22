#!/usr/bin/env python
from sys import argv as A
from math import sqrt
fh = open("flenDist.txt")
for line in fh:
   weights = line.split()
total = 0
x = float(1)
mean = float(0)
stdt = float(0)
print(len(weights))
for weight in weights:
   weight = float(weight)
   total += weight
   mean += x*weight
   x+=1
x = 0
for weight in weights:
   weight = float(weight)
   x += 1
   std1 = weight*(x-mean)**2
   stdt += std1
std = sqrt(stdt/((x-1)/x))
print("Mean:", mean)
print("STD:", std)
