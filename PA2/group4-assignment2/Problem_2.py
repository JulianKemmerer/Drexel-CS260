#
#	Programming Assignment 2
#
#	Problem 2  (15 Points)
#
#	For Dictionary ADT implemented with open hash tables the average number of probes
#	required to make either a deletion or an insertion is O(1+a).
#	Find best numerical constants for deletion and insertion.
#

class Dictionary:
	'Dictionary ADT implemented using an open hash table'
	
	def __init__(self, buckets):
		self.table = [[]] * buckets
		
	def __getitem__(self, key):
		i = self._getHash(key)
		while len(self.table[i]) > 0:
			if self.table[i][0] == key:
				return self.table[i][1]
			else:
				i += 1
		raise IndexError, 'Key not found'
		
	def _getHash(self, x):
		return ord(x[0]) % len(self.table)
	
	def insert(self, key, value):
		i = self._getHash(key)
		count = 0
		while len(self.table[i]) > 0:
			if count > len(self.table):
				raise IndexError, 'Hash table is full'
			i = i+1 if i < (len(self.table) - 1) else 0
			count += 1
		self.table[i] = [key, value]

	def delete(self, key):
		i = self._getHash(key)
		while len(self.table[i]) > 0:
			if self.table[i][0] == key:
				self.table[i] = []
				return True
			else:
				i += 1
		raise IndexError, 'Key not found'


if __name__ == '__main__':
	d = Dictionary(256)
	
	# Insert data
	print 'Inserting values'
	d.insert('Key', 'Value')
	d.insert('Other', 'Other value')
	print '\nThe value of \'Key\' is :', d['Key']
	
	# Delete data
	print '\nDeleting \'Key\' from dictionary'
	d.delete('Key')
	try:
		print 'The value of \'Key\' is :', d['Key']
	except:
		print 'Unable to find node; deletion successful.'
		
	# Explain best case
	print '\nThe best case for insertion/deletion of a node is one probe. In the above example with ' + \
		  'only one value in the dictionary, it only has to probe one value at the location returned ' + \
		  'by the hash function'
	