class node():
   def __init__(self,value):
      self.value = value
      self.right = None
      self.left = None

class binaryTree():
   def __init__(self,value):
      self.root = node(value)

   def preorder(self,start,traversal = []):
      if start is None:
         return
      
      # Root -> Left -> Right
      traversal.append(start.value)
      self.preorder(start.left,traversal)
      self.preorder(start.right,traversal)
      return traversal
   
   def inorder(self,start,traversal = []):
      if start is None:
         return
      
      #  Left -> Root -> Right
      self.inorder(start.left,traversal)
      traversal.append(start.value)
      self.inorder(start.right,traversal)
      return traversal
   
   def postorder(self,start,traversal = []):
      if start is None:
         return
      
      #  Left -> Right -> Root
      self.postorder(start.left,traversal)
      self.postorder(start.right,traversal)
      traversal.append(start.value)
      return traversal

tree = binaryTree(3)

tree.root.left = node(4)
tree.root.left.left = node(6)
tree.root.left.right = node(7)

tree.root.right = node(5)
tree.root.right = node(8)
tree.root.right = node(9)

print (tree.preorder(tree.root))

print (tree.inorder(tree.root))

print (tree.postorder(tree.root))

"""
Time Complexity = O(n)

Space Complexity 
Best Case = O(d)  d=depth
Worst Case = O(n)
"""