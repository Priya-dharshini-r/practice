# A linked list has node and each node has d1ata and next, next have the address of the next variable or it points to the next variable.
# First nodes's first data is head.
# last node's next data is NULL because, there is nothing to point to next.

# Implementation of linked list.
	# For a node we have a class Remember a node has data and next variable.
	# Create a class for Linkedlist.For a linked list we have a head which is the head or start of the linked list.

# Creating a class for node.
class Node:
	# self reference to current instance of a class,to access variable belong to the class
	# creating a method for node class and the method has data and next.
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

# Creating a class for linked list.
class LinkedList:
	def __init__(self):
		# initially we don't have any element at head so none.
		self.head = None
	# for inserting element in the linkedlist at begining, create insert at begining
	def insert_at_begining(self, data):
		# Incase of insertion at begining, For each insertion of element at begining the head node becomes the next node.
		# So while accessing the Node, Accesssing the data and next node is given as head node.
		node = Node(data, self.head)
		self.head = node

	# Insert at End
	def insert_at_end(self, data):
		# Head is None means we insert only one element in the head, and that is the last element.
		if self.head is None:
			node = Node(data, None)
		# if itr.next has some values, I am not at end so I keep moving till when the itr.next value is Null.
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	# Printing the linked list
	def print(self):
		if self.head is None:
			print("Linked list is Empty")
			return
		itr = self.head
		llstr = ""
		while itr:
			llstr += str(itr.data) + "-->"
			itr = itr.next
		print(llstr)

	# Inserting a list of values
	def insert_values(self, data_list):
		for data in data_list:
			self.insert_at_end(data)

	# Length of the linkedlist
	def length(self):
		count = 0
		itr = self.head
		while itr:
			count = count+1
			itr = itr.next
		return count

	# Removing in linked list
	def remove(self, index):
		if index<0 or index>=self.length():
			print("Invalid")

		if index == 0:
			self.head = self.next
			return
		count = 0
		itr = self.head
		while itr:
			if count == index - 1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count = count + 1

	# Insert at given position
	def insert(self, index, data):
		if index<0 or index>=self.length():
			print("Invalid")

		if index == 0:
			self.insert_at_begining(data)

		count = 0
		itr = self.head
		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				itr.next = node
				break
			itr = itr.next
			count = count+1

	# Search in Linkedlist
	def search(self, data):
		index = 0
		itr = self.head
		while itr:
			if itr.data == data:
				print(index)
				print("Found")
				break
			index = index+1
			itr = itr.next


if __name__ == "__main__":
	ll = LinkedList()
	ll.insert_at_begining(5)
	ll.insert_at_begining(89)
	ll.insert_at_end(88)
	ll.insert_at_end(100)
	ll.insert_values(["a","b"])
	ll.insert(0,1)
	ll.insert(5,"c")
	ll.search("c")
	ll.print()
	op = ll.length()
	print(op)

