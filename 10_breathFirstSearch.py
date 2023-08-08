class queue():
   def __init__(self):
      self.items = []
   
   def enqueue(self,item):
      self.items.append(item)

   def dequeue(self):
      if len(self.items):
         return(self.items.pop(0))
   
   def peek(self):
      if len(self.items):
         return(self.items[0].value)
      

class node():
   def __init__(self,value):
      self.value = value
      self.right = None
      self.left = None

class binaryTree():
   def __init__(self,value):
      self.root = node(value)

   def levelOrder(self,start):
      if start is None:
         return
      
      que = queue()
      que.enqueue(start)
      traversed = []

      while len(que.items) > 0:
         traversed.append(que.peek())
         node = que.dequeue()

         if node.left:
            que.enqueue(node.left)
         if node.right:
            que.enqueue(node.right)
      
      return traversed

tree = binaryTree(3)

tree.root.left = node(4)
tree.root.left.left = node(6)
tree.root.left.right = node(7)

tree.root.right = node(5)
tree.root.right = node(8)
tree.root.right = node(9)


print(tree.levelOrder(tree.root))

"""
Time Complexity = O(n)

Space Complexity  = O(n)
"""