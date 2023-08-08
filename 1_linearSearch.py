def linearSerach(myArray,target):
   for i in range(len(myArray)):
      if myArray[i] == target:
         return i
   return -1

print(linearSerach([1,2,3,4,5,6],3))


"""
Time Complexity
Worst case = O(n)
Best case = O(1)
Avg case = O(n)

Space Complexity = O(1)
"""
