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
from time import clock, time # for timing
from binModule import Bin

print "\n\n"

# Get the capacity for the bins from the user
cap = binModule.getCap()
allItems = binModule.getItems()
items = sorted(allItems)
bigItem = items.pop() # We can reduce time by a factor of 2 by always putting the same item in bin0
maxBins = len(allItems)
minBins = int(math.ceil(sum(allItems)/cap))
curMin = maxBins + 1
config = []

print "Your items are:", allItems, "\nYour bins have capacity", cap, "\n"
print "MIN number of bins feasible:", int(minBins), "\nMAX number of bins (i.e. # items)", maxBins, "\n\n"

def easyCase(aList):
	for item in aList:
		if item < cap/2:
			return False
	return True

def checkInput(aList):
	for item in aList:
		if item > cap:
				print "SOME ITEM WON'T EVEN FIT IN ITS OWN BIN! ABORTING"
				sys.exit()

# Begin timing
t1 = clock()

# Make sure no item is too large
checkInput(allItems)

# Check if we're in the case where all items need their own bins
if easyCase(allItems):
	print "Easy case"
	curMin = len(allItems)
	for item in allItems:
		config.append([item])

else:
	# Iterate through the permutations of the items
	for x in itertools.permutations(items):
		bins = []										# Clear the list of bins out after each new permuatation
		Binny = Bin(cap, [bigItem])	# A bin to begin your packing
		bins.append(Binny)
		# Iterate through each item in this permutation
		for item in x:						
			# Don't bother finding out how to fit items if it's not better
			if len(bins) >= curMin:
				break
			# Still room in this bin? 
			if Binny.free_capacity() >= item:
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

# End timing
t2 = clock()
print "Algorithm runtime (s):", t2-t1

remaining = [xBin.free_capacity() for xBin in bins]
capacity_left = sum(remaining)
capacity_total = sum([xBin.capacity for xBin in bins])
capacity_used = capacity_total - capacity_left

# Put the item we removed back in so it looks pretty
items.append(bigItem)
print "True Bin Packing for", items, "with capacity", cap, "used", curMin, "bins"
print "A configuration that worked was:", config
print "Capacity remaining per bin: ", remaining
print "Total capacity used:", capacity_used
print "Total capacity remaining: ", capacity_left
print "Efficiency (%): ", 100 * (1 - capacity_left/float(capacity_total))
