def mergeSort(arr):
   if len(arr) == 1 :
      return arr
   
   middle = len(arr)//2
   left = arr[:middle]
   right = arr[middle:]

   leftResult = mergeSort(left)
   rightResult = mergeSort(right)

   return merge(leftResult,rightResult)

def merge(leftResult,rightResult):
   result = [None] * (len(leftResult) + len(rightResult))
   i = j = k = 0

   while i < len(leftResult) and j < len(rightResult):
      if leftResult[i] <= rightResult[j]:
         result[k] = leftResult[i]
         i+=1
      else:
         result[k] = rightResult[j]
         j+=1
      k+=1

   while i < len(leftResult):
      result[k] = leftResult[i]
      i+=1
      k+=1

   while j < len(rightResult):
      result[k] = rightResult[j]
      j+=1
      k+=1
   
   return result


print(mergeSort([4,1,3,6,2]))

"""
Time Complexity
Worst case = O(n(log(n)))
Best case = O(n(log(n)))
Avg case = O(n(log(n)))

Space Complexity = O(n)
"""