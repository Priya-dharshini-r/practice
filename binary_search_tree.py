class Node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			node = Node(data, None, None)
			self.root = node
		else:
			itr = self.root
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

				elif data > itr.data and itr.right is not None:
					itr = itr.right

	def search(self, search_data):
		if search_data == self.root.data:
			print("Element found at root node")
		else:
			itr = self.root
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
		if self.root is None:
			print("Tree is Empty")
		else:
			itr = self.root
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
		if self.root is None:
			print("Deletion, is not possible!")
		else:
			itr = self.root
			itr_parent = None
			while itr:
				if delete_data == itr.data:

					if itr.left is None and itr.right is None:
						if delete_data < itr_parent.data:
							itr_parent.left = None
						else:
							itr_parent.right = None
					elif itr.left is not None and itr.right is not None:
						print("This case is for node with two child")
						right_subtree_minimum = self._return_minimum(itr.right)
						self.delete(right_subtree_minimum.data)
						itr.data = right_subtree_minimum.data

					# Case with only left child or only right child

					elif itr.left is None and itr.right is not None: # It has right child in it
						print("This case is for node with one child and left is empty")
						if delete_data > itr_parent.data:
							itr_parent.right = itr.right
						else:
							itr_parent.left = itr.right

					elif itr.left is not None and itr.right is None:
						print("This case is for with one left child and right is empty")
						if delete_data < itr_parent.data:
							itr_parent.left = itr.left
						else:
							itr_parent.right = itr.left

					break

				elif delete_data < itr.data:
					itr_parent = itr
					itr = itr.left
				elif delete_data > itr.data:
					itr_parent = itr
					itr = itr.right
			else:
				print("Element is not in tree!")



	def _return_minimum(self, node):
		itr = node
		while itr:
			if itr.left is None:
				return itr
			else:
				itr = itr.left


	def _inorder_traversal(self, node):
		if node.left is not None:
			self._inorder_traversal(node.left)

		print(node.data, end = " ")

		if node.right is not None:
			self._inorder_traversal(node.right)

	def _preorder_traversal(self, root):
		if root:
			print(root.data,"-->", end = " ")
			self._preorder_traversal(root.left)
			self._preorder_traversal(root.right)



	def print(self):
		if self.root is None:
			print("Not Possible")

		else:
			self._inorder_traversal(self.root)

		print()

	def print_preorder(self):
		if self.root is None:
			print("Tree is empty")

		else:
			self._preorder_traversal(self.root)

		print()



if __name__ == "__main__":
	bst = BinarySearchTree()
	bst.insert(43)
	bst.insert(10)
	bst.insert(79)
	bst.insert(90)
	bst.insert(12)
	bst.insert(54)
	bst.insert(11)
	bst.insert(9)
	bst.insert(50)
	bst.print()
	bst.delete(43)
	bst.print()
	bst.print_preorder()
	bst1 = BinarySearchTree()
	bst1.insert(3)
	bst1.insert(9)
	bst1.insert(20)
	bst1.insert(15)
	bst1.insert(7)
	# bst1.insert(2)
	# bst1.insert(13)
	# bst1.insert(4)
	# bst1.insert(1)
	bst1.print()
	bst1.print_preorder()
	# bst.delete(90)
	# bst.print()
	# bst.delete(12)
	# bst.print()
	# bst.delete(54)
	# bst.print()
	# bst.delete(79)
	# bst.print()
	bst2 = BinarySearchTree()
	bst2.insert(5)
	bst2.insert(4)
	bst2.insert(8)
	bst2.insert(11)
	bst2.insert(13)
	bst2.insert(4)
	bst2.insert(7)
	bst2.insert(2)
	bst2.insert(1)
	bst2.print()
	bst2.print_preorder()








