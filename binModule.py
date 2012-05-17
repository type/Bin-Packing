class Bin:
	"""Bin for holding items"""
	def __init__(self, capacity, contents=[]):
		self.capacity = capacity
		self.contents = contents
	def add(self, x):
		self.contents.append(x)
	def __repr__(self):
		return str(self.contents)

def getCap():
	while True:
		try:
			cap = float(raw_input('Enter the capacity of the bins (ex: 5): ').strip())
			break
		except ValueError:
			print "You didn't enter input correctly!"
	return cap

# Get the items from the user
def getItems():
	while True:
		try: 
			items = [float(n) for n in raw_input('Enter the items\' weights separated by spaces (ex: 2 4 3): ').strip().split(' ')]
			break
		except ValueError:
			print "You didn't enter input correctly!"
	return items
