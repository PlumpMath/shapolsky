#!/usr/bin/python
import csv
from itertools import groupby, combinations
from collections import defaultdict

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

with open('real-property-parties.csv') as csvfile:
	reader = csv.reader(csvfile)
	partiesList = list(reader)[1:]


"""
print map(lambda x: x[3], partiesList)
print len(map(lambda x: x[3], partiesList))
print len(set(map(lambda x: x[3], partiesList)))
"""

adjs = []

for key, group in groupby(partiesList, lambda x: x[0]):
	print "----" , key
	peopleInvolved = [thing[3] for thing in group]
	adjForTransaction = map(lambda x: list(x) + [key], list(combinations( peopleInvolved , 2)))
#	adjs += adjForTransaction 
	adjs += [peopleInvolved[:2] + [key]]

print adjs

with open('real-property-parties.adjacency.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(["source", "target", "ID"])
	for line in adjs:
		writer.writerow(line)



