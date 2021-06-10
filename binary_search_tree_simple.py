class Node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self):
		self.head = None

	def insert(self, data):
		if self.head is None:
			node = Node(data, None, None)
			self.head = node
		else:
			if data < self.head.data and self.head.left is None:
				left_node = Node(data, None, None)
				self.head.left = left_node

			elif data > self.head.data and self.head.right is None:
				right_node = Node(data, None, None)
				self.head.right = right_node


	def print(self):
		if self.head is None:
			print("Not Possible")

		else:
			if self.head.left is None and self.head.right is None:
				print(self.head.data)
			elif self.head.right is None:
				print(self.head.left.data, self.head.data)
			elif self.head.left is None:
				print(self.head.data, self.head.right.data)
			else:
				print(self.head.left.data, self.head.data, self.head.right.data)




if __name__ == "__main__":
	bst = BinarySearchTree()
	bst.insert(43)
	bst.print()
	bst.insert(10)
	bst.print()
	bst.insert(79)
	bst.print()
