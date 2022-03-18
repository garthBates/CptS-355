# CptS 355 - Fall 2020 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework
# Garth Bates
# 11473063

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1-a) getNumCases - 10%
def getNumCases(data, counties, months):
		total = 0
		for places in counties:
			for i in range(0, len(months)):
				total += data[places].get(months[i])
		return total


## problem 1-b) getMonthlyCases - 15%
from functools import reduce
def getMonthlyCases(data):
	newData = {}
		counties = list(data.keys())
		#print(counties)
		cases = list(data.values())
		for places in counties:
			months = list(data[places].keys())
			#print(months)
			#print(data[places])
			for dates in months:
				newData[dates] = {}
				newData[dates][places] = newData[dates].get(places)
				#newData[dates][places] = data[places][dates]
				#print(data[places][dates])
		return newData

## problem 1-c) mostCases - 15%


## problem 2a) searchDicts(L,k) - 5%
def searchDicts(L, k):
	if k in L:
		value = L.get(k)
		if value is not None:
			return value
	if (isinstance (L, list)):
		for dicts in reversed(L):
			return searchDicts(dicts, k)

## problem 2b) searchDicts2(L,k) - 10%
def searchDicts2(L, k):


def searchDictsHelper(L, k, index):
     

## problem 3 - adduptoZero - 10%
from itertools import combinations
def adduptoZero(L, n):
	    zeros = []
	    combos = list(combinations(L, n))
	    for i in range(0, len(combos)):
		    if (sum(list(combos[i])) == 0):
			    zeros.append(list(combos[i]))
	    return zeros
     

## problem 4 - getLongest - 10%
def getLongest(L):
	if (isinstance(L, list) == True):
		#getLongest(L[1:])
		max (L, getLongest(L[1:]))
		print(L[0])
	#else:
		#print(L[1:])
		#max (len(L), getLongest(L[1:]))

## problem 5 - apply2nextN - 20%
class apply2nextN():
     def __init__(self):
          self.current = a
     
     def __iter__(self):
          return self

     
     def __next__(self):
          n = self.current
          self.current += 1
          return n
