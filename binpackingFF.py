# First-fit approximation algorithm for Bin Packing
import math
import sys
import binModule
from time import time, clock
from binModule import Bin

print "\n\n"

# Get the capacity for the bins from the user
cap = binModule.getCap()
# Get the items from the user
items = binModule.getItems()

maxBins = len(items)
minBins = int(math.ceil(sum(items)/cap))
bins = []

print "Your items are:", items, "\nYour bins have capacity", cap, "\n"
print "MIN number of bins feasible:", int(minBins), "\nMAX number of bins (i.e. # items)", maxBins, "\n\n"

bins.append(Bin(cap, [])) # we need at least one bin to begin

t1 = clock()
for item in items:
	# Add the item to the first bin that can hold it
	# If no bin can hold it, make a new bin
	if item > cap:  
		print "SOME ITEM WON'T EVEN FIT IN ITS OWN BIN! ABORTING"
		sys.exit()
	for xBin in bins:
		if xBin.free_capacity() >= item:
			xBin.add(item)
			break
		if bins.index(xBin) == len(bins) - 1:
			bins.append(Bin(cap, []))

t2 = clock()
print "Algorithm runtime (s):", t2 - t1

remaining = [xBin.free_capacity() for xBin in bins]
capacity_left = sum(remaining)
capacity_total = sum([xBin.capacity for xBin in bins])
capacity_used = capacity_total - capacity_left

print "First-fit algorithm for", items, "with capacity", cap, "used", len(bins), "bins"
print "The configuration was", bins
print "Capacity remaining per bin: ", remaining
print "Total capacity used:", capacity_used
print "Total capacity remaining: ", capacity_left
print "Efficiency (%): ", 100 * (1 - capacity_left/float(capacity_total))

