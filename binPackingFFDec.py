# First-fit Decreasing approximation algorithm for Bin Packing
import math
import sys
import binModule
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

items = sorted(items)			# sort ascending

for item in reversed(items): #iterate through the list backwards
	# Add the item to the first bin that can hold it
	# If no bin can hold it, make a new bin
	if item > cap:  
		print "SOME ITEM WON'T EVEN FIT IN ITS OWN BIN! ABORTING"
		sys.exit()
	for xBin in bins:
		if xBin.capacity - sum(xBin.contents) >= item:
			xBin.add(item)
			break
		if bins.index(xBin) == len(bins) - 1:
			bins.append(Bin(cap, []))

print "First-fit Decreasing algorithm for", items, "with capacity", cap, "used", len(bins), "bins"
print "The configuration was", bins
