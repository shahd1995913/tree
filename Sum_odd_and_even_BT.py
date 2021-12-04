

# create Tree
# to create a new BST node
class newNode:

	# Construct to create a new node
	def __init__(self, value):

		self.value = value
		
		self.left = None
		
		self.right = None

# A utility function to do inorder
# traversal of BST

def inorder( root) :
	

	if (root != None):

		inorder(root.left)


		print(root.value, end = " ")

		inorder(root.right)
	
""" A utility function to insert a
new node with given value in BST """
def insert(node, value):

	""" If the tree is empty,
	return a new node """
	if (node == None):
		return newNode(value)

	""" Otherwise, recur down the tree """
	if (value < node.value):
		node.left = insert(node.left, value)
	else:
		node.right = insert(node.right, value)

	""" return the (unchanged) node pointer """

	return node
arr=[]
x =0
# Function to print all even nodes
def oddNode(root) :
	if (root != None):
		oddNode(root.left)		
		# if node is odd then print it
		if (root.value % 2 != 0):
			
			arr.append(root.value)

		oddNode(root.right)	
		return((arr))

arr_even=[]	

def evenNode(root) :
	if (root != None):
		evenNode(root.left)		
		# if node is odd then print it
		if (root.value % 2 == 0):
			
			arr_even.append(root.value)

		evenNode(root.right)	
		return((arr_even))		    


	

# Driver Code
if __name__ == '__main__':
	
	""" Let us create following BST
	5
	/ \
	3   7
	/ \ / \
	2 4 6 8 """
	root = None
	root = insert(root, 5)
	root = insert(root, 5)
	root = insert(root, 2)
	root = insert(root, 2)
	root = insert(root, 1)
	root = insert(root, 10)
	root = insert(root, 2)

	sum_odd_node=oddNode(root)
	print("The sum for odd node ",sum(sum_odd_node))

	sum_even_node =evenNode(root)
	print("The sum for even Node ", sum(sum_even_node))


