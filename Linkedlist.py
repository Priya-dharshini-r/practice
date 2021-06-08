class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_head(self, data):
		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			node = Node(data, next = None)
			self.head = node

		else:
			node = Node(data, next = None)
			itr = self.head
			while itr.next != None:
				itr = itr.next
			itr.next = node

	def delete(self, data):
		if self.head is None:
			print("Linkedlist is empty so deletion is not possible")

		elif self.head.data == data:
			self.head = self.head.next

		else:
			itr = self.head
			while itr.next != None:
				if data == itr.next.data:
					itr.next = itr.next.next
					break
				itr = itr.next

	def search(self, data):
		if self.head is None:
			print("Search not Possible")

		else:
			itr = self.head
			while itr.next != None:
				if itr.data == data:
					print("Element Found")
					break
				else:
					print("Element Not Found")
					break
				itr = itr.next

	def insert_at_middle(self, data, newdata):
		itr = self.head
		print("Data", data, "Newdata:", newdata)
		while itr:
			print("itr_data:", itr.data)
			if itr.data == data:
				node = Node(newdata, itr.next)
				print("Current_data:", data, "Next_data:", itr.next)
				itr.next = node
				print("Node",node.data)
				break
			itr = itr.next


	def print(self):
		if self.head is None:
			print("LinkedList is Empty!")
		output = ""
		itr = self.head
		while itr:
			output += str(itr.data) + "-->"
			itr = itr.next

		return output

if __name__ == "__main__":
	linkedlist = LinkedList()
	linkedlist.insert_at_head(100)
	linkedlist.insert_at_head(50)
	# op1 = linkedlist.print()
	# print(op1)
	linkedlist.insert_at_end(200)
	# op2 = linkedlist.print()
	# print(op2)
	linkedlist.insert_at_end(7)
	# linkedlist.search("c")
	# linkedlist.delete(100)
	# linkedlist.delete(50)
	linkedlist.insert_at_middle(100, 150)
	op = linkedlist.print()
	print(op)
