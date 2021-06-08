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
			itr = self.head
			while itr:
				if data < itr.data and itr.left is None:
					left_node = Node(data, None, None)
					itr.left = left_node
					break

				elif data > itr.data and itr.right is None:
					right_node = Node(data, None, None)
					itr.right = right_node
					break

				elif data < itr.data and itr.left is not None:
					itr = itr.left

				elif data > itr.data and itr.left is not None:
					itr = itr.right

	def _inorder_traversal(self, node):
		if node.left is not None:
			self._inorder_traversal(node.left)

		print(node.data, end = " ")

		if node.right is not None:
			self._inorder_traversal(node.right)



	def print(self):
		# self._inorder_traversal(self.head)
		if self.head is None:
			print("Not Possible")

		else:
			self._inorder_traversal(self.head)

		print()
		# else:
		#	if self.head.left is None and self.head.right is None:
		#		print(self.head.data)
		#	elif self.head.right is None:
		#		print(self.head.left.data, self.head.data)
		#	elif self.head.left is None:
		#		print(self.head.data, self.head.right.data)
		#	else:
		#		print(self.head.left.data, self.head.data, self.head.right.data)



if __name__ == "__main__":
	bst = BinarySearchTree()
	bst.insert(43)
	bst.print()
	bst.insert(10)
	bst.print()
	bst.insert(79)
	bst.print()
	bst.insert(90)
	bst.print()
