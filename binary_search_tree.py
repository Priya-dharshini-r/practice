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

	def search(self, search_data):
		if search_data == self.head.data:
			print("Element found at root node")
		else:
			itr = self.head
			while itr:
				if search_data < itr.data:
					itr = itr.left
					if itr != None and itr.data == search_data:
						print("Element found at left")
						break
				elif search_data > itr.data:
					itr = itr.right
					if itr != None and itr.data == search_data:
						print("Element found at right")
						break
			else:
				print("Element is not in tree")


	def search_two(self, search_data):
		if self.head is None:
			print("Tree is Empty")
		else:
			itr = self.head
			while itr:
				if search_data == itr.data:
					print("Element found")
					break
				elif search_data < itr.data:
					itr = itr.left
				elif search_data > itr.data:
					itr = itr.right
			else:
				print("Not found")

	def delete(self, delete_data):
		if self.head is None:
			print("Deletion, is not possible!")
		else:
			itr = self.head
			while itr:
				if delete_data == itr.data:

					if itr.left is None and itr.right is None:
						print("This case is for leaf node")
					elif itr.left is not None and itr.right is not None:
						print("This case is for leaf with two child")
					else:
						print("This case is for leaf with one child")
					break

				elif delete_data < itr.data:
					itr = itr.left
				elif delete_data > itr.data:
					itr = itr.right
			else:
				print("Element is not in tree!")



	def _inorder_traversal(self, node):
		if node.left is not None:
			self._inorder_traversal(node.left)

		print(node.data, end = " ")

		if node.right is not None:
			self._inorder_traversal(node.right)



	def print(self):
		if self.head is None:
			print("Not Possible")

		else:
			self._inorder_traversal(self.head)

		print()


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
	bst.insert(11)
	bst.insert(1)
	bst.insert(20)
	bst.print()
	bst.search_two(1)
	bst.search_two(10)
	bst.search_two(20)
	bst.search_two(11)
	bst.search_two(90)
	bst.search_two(79)
	bst.search_two(43)
	bst.search_two(100)
	bst.delete(43)
	bst.delete(20)
	bst.delete(11)
