# A true (exponential time) algorith for the bin packing problem
# Takes in a capacity (float) for each of the bins (each has same capacity) and a list of items (floats)
# that must be packed
# Prints out the minimum number of bins for the given input as well as a configuration that 
# yielded the minimum 

import math				# for ceil
import itertools	# for permutation iterator
import copy				# for deepcopying Bins
import sys				# for exit
import binModule
from binModule import Bin

print "\n\n"

# Get the capacity for the bins from the user
cap = binModule.getCap()
items = binModule.getItems()

maxBins = len(items)
minBins = int(math.ceil(sum(items)/cap))
curMin = maxBins + 1
config = []

print "Your items are:", items, "\nYour bins have capacity", cap, "\n"
print "MIN number of bins feasible:", int(minBins), "\nMAX number of bins (i.e. # items)", maxBins, "\n\n"

# Iterate through the permutations of the items
for x in itertools.permutations(items):
	bins = []							# Clear the list of bins out after each new permuatation
	Binny = Bin(cap, [])	# A bin to begin your packing
	bins.append(Binny)
	# Iterate through each item in this permutation
	for item in x:						
		# Don't bother finding out how to fit items if it's not better
		if len(bins) >= curMin:
			break
		if item > cap:
			print "SOME ITEM WON'T EVEN FIT IN ITS OWN BIN! ABORTING"
			sys.exit()
		# Still room in this bin? 
		if Binny.capacity - sum(Binny.contents) >= item:
			Binny.add(item)
		# No...we need a fresh bin
		else:
			Binny = Bin(cap, [])
			Binny.add(item)
			bins.append(Binny)
	# We've put all the items in the perm into bins...
	# If we've reached a new minimum of bins used, save the
	# minimum and keep a "proof" copy of the configuration that worked
	if len(bins) < curMin:
		curMin = len(bins)
		config = copy.deepcopy(bins)
	# If we used the true minimum number of bins, we're definitely done
	if len(bins) == minBins:
		break

print "True Bin Packing for", items, "with capacity", cap, "used", curMin, "bins"
print "A configuration that worked was:", config
