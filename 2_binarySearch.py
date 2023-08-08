def binarySearch(myArray,target):
   left = 0
   right = len(myArray)-1

   while left <= right:
      middle = (left+right)//2
      middleElement = myArray[middle]
      if target == middleElement:
         return middle
      elif target < middleElement:
         right = middle - 1
      else:
         left = middle + 1
      
   return -1

print(binarySearch([1,2,3,4,5,6,7,8,9],0))

"""
Time Complexity
Worst case = O(log(n))
Best case = O(1)
Avg case = O(log(n))

Space Complexity = O(1)
"""
