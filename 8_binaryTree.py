class node():
   def __init__(self,value):
      self.value = value
      self.right = None
      self.left = None

class binaryTree():
   def __init__(self,value):
      self.root = node(value)

tree = binaryTree(3)

tree.root.left = node(4)
tree.root.left.left = node(6)
tree.root.left.right = node(7)

tree.root.right = node(5)
tree.root.right = node(8)
tree.root.right = node(9)