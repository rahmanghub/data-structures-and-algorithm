def bubbleSort(myArray):
   for iter in range(len(myArray)):
      for index in range(len(myArray) - 1 - iter):
         if myArray[index] > myArray[index + 1]:
            myArray[index],myArray[index+1] = myArray[index+1],myArray[index]
   return myArray
               
print(bubbleSort([2,10,1,3,7,0]))

"""
Time Complexity
Worst case = O(n^2)
Best case = O(n)
Avg case = O(n^2)

Space Complexity = O(1)
"""
