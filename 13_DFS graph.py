class Node():
   def __init__(self,value):
      self.value = value
      self.adjacent = []
      self.visited = False

class Graph():
   def DFS(self,start,traversal = []):
      start.visited = True
      traversal.append(start.value)

      for element in start.adjacent:
         if element.visited is False:
            self.DFS(element,traversal)  
      return traversal


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')

node1.adjacent.append(node2)
node1.adjacent.append(node3)
node1.adjacent.append(node4)
node2.adjacent.append(node5)
node2.adjacent.append(node6)
node4.adjacent.append(node7)

graph = Graph()
print(graph.DFS(node1))


"""
Time Complexity = O(v+e)  v=vertex , e=edge

Space Complexity  = O(v)
"""