"""
This is my attempt to create a list class
LinkedList has every method List does except for sort.
It also has a method list doesnt have, prepend.
This list is double linked and will travel the 'shortest distace' to get to the elements.
Slicing has been overridden and I have done tests with no errors so far.

This was just a test of my programming skills as I wrote this to challenge myself.
I got minor help from:
	http://www.siafoo.net/article/57

This website has all built in methods and their expected returns and calls so I knew what to
override. I also used:
	https://docs.python.org/3/tutorial/datastructures.html
to get a list of the methods that list has. 

Other than those two I didn't use any online sources
to write this 400 line monstrosity (part of the test to not go off of sample code)
"""


class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

	def __str__(self):
		p = self.prev.data if self.prev else "None"
		n = self.next.data if self.next else "None"
		return "({} < {} > {})".format(p, self.data, n)

	def setData(self, data):
		self.data = data

	def setNext(self, nextNode):
		self.next = nextNode

	def setPrev(self, prevNode):
		self.prev = prevNode


class LinkedList():

	def __init__(self):
		self.head = None
		self.tail = None
		self.curpos = None
		self.len = 0

	def __len__(self):
		return self.len

	def __contains__(self, item):
		if self.head == None:
			return False
		elif self.head == self.tail:
			return item == self.head.data
		else:
			curNode = self.head
			while curNode != None:
				if curNode.data == item:
					return True
				curNode = curNode.next
			return False

	def __iter__(self):
		self.curpos = self.head
		return self

	def __next__(self):
		if self.curpos == None:
			raise StopIteration
		data = self.curpos.data
		self.curpos = self.curpos.next
		return data

	def __getitem__(self, key):
		if type(key) == slice:

			start = key.start
			stop = key.stop
			step = key.step
			
			if step == None: step = 1

			if start and start >= len(self):
				raise IndexError("list start index out of range")

			if stop and stop > len(self):
				raise IndexError("list stop index out of range")
			
			if start and start < 0:
				start = self.len - ((start * -1) % self.len)
			if stop and stop < 0:
				stop = self.len - ((stop * -1) % self.len)

			if step > 0:
				if start == None: start = 0
				if stop == None: stop = self.len
			elif step < 0:
				if start == None: start = self.len - 1
				if stop == None: stop = -1
			else:
				raise ValueError("slice step cannot be zero")

			ret = LinkedList()

			alt_start = len(self) - start - 1

			if start <= alt_start:
				curNode = self.head
				for i in range(start):
					curNode = curNode.next
			else:
				curNode = self.tail
				for i in range(alt_start):
					curNode = curNode.prev

			if step > 0:
				for i in range(start, stop, step):
					if curNode == None:
						break
					ret.append(curNode.data)
					for i in range(step):
						if curNode == None:
							break
						curNode = curNode.next

			else:
				posi_step = step * -1
				if stop > start: stop = -1
				for i in range(start, stop, step):
					if curNode == None:
						break
					ret.append(curNode.data)
					for i in range(posi_step):
						if curNode == None:
							break
						curNode = curNode.prev

			return ret

		elif type(key) == int:
			if key >= len(self):
				raise IndexError("list index out of range")

			if key < 0:
				key = self.len - ((key * -1) % self.len)

			alt_key = len(self) - key - 1

			if key <= alt_key:
				curNode = self.head
				for i in range(key):
					curNode = curNode.next
			else:
				curNode = self.tail
				for i in range(alt_key):
					curNode = curNode.prev

			return curNode.data

		else:
			raise TypeError("list indices must be integers or slices, not float")

	def __setitem__(self, key, value):
		if key >= len(self):
			raise IndexError("list index out of range")

		if key < 0:
			key = self.len - ((key * -1) % self.len)

		alt_key = len(self) - key - 1

		if key <= alt_key:
			curNode = self.head
			for i in range(key):
				curNode = curNode.next
		else:
			curNode = self.tail
			for i in range(alt_key):
				curNode = curNode.prev

		curNode.data = value

	def __delitem__(self, key):
		if type(key) == slice:

			start = key.start
			stop = key.stop
			step = key.step
			
			if step == None: step = 1

			if start and start >= len(self):
				raise IndexError("list start index out of range")

			if stop and stop > len(self):
				raise IndexError("list stop index out of range")
			
			if start and start < 0:
				start = self.len - ((start * -1) % self.len)
			if stop and stop < 0:
				stop = self.len - ((stop * -1) % self.len)

			if step > 0:
				if start == None: start = 0
				if stop == None: stop = self.len
			elif step < 0:
				if start == None: start = self.len - 1
				if stop == None: stop = -1
			else:
				raise ValueError("slice step cannot be zero")

			alt_start = len(self) - start - 1

			if start <= alt_start:
				curNode = self.head
				for i in range(start):
					curNode = curNode.next
			else:
				curNode = self.tail
				for i in range(alt_start):
					curNode = curNode.prev

			if step > 0:
				for i in range(start, stop, step):
					if curNode == None:
						break
					if curNode == None:
						break
					if self.head == self.tail:
						if self.head != None:
							self.head = None
							self.tail = None

					elif self.head == curNode:
						self.head = curNode.next
						self.head.prev = None

					elif self.tail == curNode:
						self.tail = curNode.prev
						self.tail.next = None

					else:
						curNode.prev.next = curNode.next
						curNode.next.prev = curNode.prev
						
					self.len -= 1

					for i in range(step):
						if curNode == None:
							break
						curNode = curNode.next

			else:
				posi_step = step * -1
				if stop > start: stop = -1
				for i in range(start, stop, step):
					if curNode == None:
						break
					if self.head == self.tail:
						if self.head != None:
							self.head = None
							self.tail = None

					elif self.head == curNode:
						self.head = curNode.next
						self.head.prev = None

					elif self.tail == curNode:
						self.tail = curNode.prev
						self.tail.next = None

					else:
						curNode.prev.next = curNode.next
						curNode.next.prev = curNode.prev

					self.len -= 1

					for i in range(posi_step):
						if curNode == None:
							break
						curNode = curNode.prev

		elif type(key) == int:
			if key >= len(self):
				raise IndexError("list index out of range")

			if key < 0:
				key = self.len - ((key * -1) % self.len)

			alt_key = len(self) - key - 1

			if key <= alt_key:
				curNode = self.head
				for i in range(key):
					curNode = curNode.next
			else:
				curNode = self.tail
				for i in range(alt_key):
					curNode = curNode.prev

			if self.head == self.tail:
				if self.head != None:
					self.head = None
					self.tail = None

			elif self.head == curNode:
				self.head = curNode.next
				self.head.prev = None

			elif self.tail == curNode:
				self.tail = curNode.prev
				self.tail.next = None

			else:
				curNode.prev.next = curNode.next
				curNode.next.prev = curNode.prev

			self.len -= 1

		else:
			raise TypeError("list indices must be integers or slices, not float")


	def __str__(self):
		s = ""
		if self.head == None:
			s = "[]"
		elif self.head == self.tail:
			s = "[{}]".format(self.head.data)
		else:
			s = "["
			curNode = self.head
			while curNode != None:
				s += "{}, ".format(curNode.data)
				curNode = curNode.next
			s = s[:-2] + "]"
		return s

	def __appendNode(self, node):
		if type(node) != Node:
			raise Exception("Type Node expected. Got {}".format(type(Node)))

		if self.head == None and self.tail == None:
			self.head = node
			self.tail = node

		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
		self.len += 1

	def __prependNode(self, node):
		if type(node) != Node:
			raise Exception("Type Node expected. Got {}".format(type(Node)))

		if self.head == None and self.tail == None:
			self.head = node
			self.tail = node

		else:
			node.next = self.head
			self.head.prev = node
			self.head = node
		self.len += 1

	def __addNode(self, node, key):
		if key >= len(self):
			raise IndexError("list index out of range")

		if key < 0:
			key = self.len - ((key * -1) % self.len)

		alt_key = len(self) - key - 1

		if key <= alt_key:
			curNode = self.head
			for i in range(key):
				curNode = curNode.next
		else:
			curNode = self.tail
			for i in range(alt_key):
				curNode = curNode.prev

		if self.head == self.tail:
			if self.head == None:
				self.head = node
				self.tail = node

		else:
			node.next = curNode
			node.prev = curNode.prev
			curNode.prev.next = node
			curNode.prev = node

		self.len += 1

	def append(self, data):
		self.__appendNode(Node(data))

	def prepend(self, data):
		self.__prependNode(Node(data))

	def extend(self, data):
		for item in data:
			self.append(item)

	def insert(self, key, item):
		if key == 0:
			self.prepend(item)
		elif key == self.len:
			self.append(item)
		else:
			self.__addNode(Node(item), key)

	def remove(self, item):
		c = 0
		for i in self:
			if i == item:
				del self[c]
				return
			c += 1
		raise ValueError("list.remove(x): x not in list")

	def pop(self, key=-1):
		data = self[key]
		del self[key]
		return data

	def clear(self):
		del self[:]

	def index(self, item, start=0, end=None):
		scope = self[start:end]

		c = start
		for i in scope:
			if i == item:
				return c
			c += 1

	def count(self, item):
		ret = 0
		for i in self:
			if i == item:
				ret += 1
		return ret

	def reverse(self):
		rev_data = self[::-1]
		self.clear()
		for i in rev_data:
			self.append(i)

	def copy(self):
		return self[:]

		

ref = list()

x = LinkedList()

for i in range(10):
	x.append(i)

for i in range(10):
	ref.append(i)

print("Basic Compares:")
print("="*20)
print(ref, len(ref))
print(x, len(x))
print(ref[3], x[3])
print("="*20)
print("Operations:")
x.append(42)
ref.append(42)
x.append(5)
ref.append(5)
print(x.pop(0), ref.pop(0))
print(x.pop(5), ref.pop(5))
del x[2]
del ref[2]
print(ref, len(ref))
print(x, len(ref))
print("="*20)
print("Slices:")
print(x[:5])
print(ref[:5])
print(x[5:])
print(ref[5:])
print(x[2:7])
print(ref[2:7])
print(x[1::2])
print(ref[1::2])
print(x[8:3:-1])
print(ref[8:3:-1])
print(x[3::-1])
print(ref[3::-1])
print(x[::-1])
print(ref[::-1])
del x[::-2]
del ref[::-2]
print(x, len(x))
print(ref, len(ref))
print("="*20)
print("High level functions:")
x.clear()
ref.clear()
print(x, len(x))
print(ref, len(ref))

for i in range(10):
	x.append(i)

for i in range(10):
	ref.append(i)

x.reverse()
ref.reverse()
print(x)
print(ref)
x.insert(0, 11)
ref.insert(0, 11)
x.insert(5, 42)
ref.insert(5, 42)
x.insert(12, 50)
ref.insert(12, 50)
print(x, len(x))
print(ref, len(ref))
print(x.index(5, 3, 8), ref.index(5, 3, 8))
print(x.count(7), ref.count(7))