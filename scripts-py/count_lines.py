#!/usr/bin/env python3

import fileinput
from collections import Counter

counts = Counter()

for line in fileinput.input():
  counts[line.strip()] += 1

print("Line\tCount")
for (k,v) in sorted(counts.items()):
  print("{0}\t{1}".format(k,v))
 
