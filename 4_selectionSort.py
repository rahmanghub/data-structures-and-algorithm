def selectionSort(arr):
   for ite in range(len(arr)):
      minX = ite
      for i in range(ite+1,len(arr)):
         if arr[i]<arr[minX]:
            minX = i            
      arr[ite],arr[minX] = arr[minX],arr[ite]

   return arr

print(selectionSort([1,8,4,5,0,2,4,6]))

"""
Time Complexity
Worst case = O(n^2)
Best case = O(n^2)
Avg case = O(n^2)

Space Complexity = O(1)
"""