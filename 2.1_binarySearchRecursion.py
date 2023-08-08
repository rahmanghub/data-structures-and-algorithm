def binarySearch(myArray,target):
   left = 0
   right = len(myArray)-1
   result = helper(myArray,target,left,right)
   return result

def helper(myArray,target,left,right):
   if left >right:
      return -1
   
   middle = (left+right)//2
   middleElement = myArray[middle]
   
   if target == middleElement:
      return middle
   elif target < middleElement:
      right = middle - 1
      return helper(myArray,target,left,right)
   else:
      left = middle + 1 
      return helper(myArray,target,left,right)
