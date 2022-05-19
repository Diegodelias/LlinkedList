

class BinaryNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class BinaryTree:
	''' A Binary Tree class '''
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		self.root = self.__insert(self.root, data)

	def __insert(self, node, data):
		if node == None:
			node = BinaryNode(data) # No node exists so we create a new node
		elif data < node.data:
			node.left = self.__insert(node.left, data) # data is smaller than the current node so go to the left
		elif data > node.data:
			node.right = self.__insert(node.right, data)
		return node

	def print_tree(self):
		self.__print_tree(self.root)

	def __print_tree(self, node):
		if node == None:
			return
		self.__print_tree(node.left)
		print node.data
		self.__print_tree(node.right)

	def max_depth(self):
		return self.__max_depth(self.root)

	def __max_depth(self, node):
		if node == None:
			return 0
		return max(self.__max_depth(node.left), self.__max_depth(node.right)) + 1 

	def exists(self, data):
		return self.__exists(self.root, data)
	
	def __exists(self, node, data):
		if node == None:
			return False
		print node.data
		if data < node.data:
			return self.__exists(node.left, data)
		elif data > node.data:
			return self.__exists(node.right, data)
		else:
			return True

	def leaf_count(self):
		return self.__leaf_count(self.root)

	def __leaf_count(self, node):
		if node == None:
			return 0
		if node.right == None and node.left == None:
			return 1
		else:
			return self.__leaf_count(node.left) + self.__leaf_count(node.right)

	def node_count(self, depth):
		return self.__node_count(self.root, depth)
	
	def __node_count(self, node, depth):
		if node == None:
			return 0
		if (depth == 0):
			return 1 # trivial case with the root being the only node
		
		return self.__node_count(node.left, depth-1) + self.__node_count(node.right, depth-1)