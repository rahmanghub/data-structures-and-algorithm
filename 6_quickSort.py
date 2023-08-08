def quickSOrt(arr):
   qshelper(arr,0,len(arr)-1)
   return arr

def qshelper(arr,start,end):
   if start >= end:
      return
   
   pivot = start
   left = start+1
   right = end

   while left <= right:
      if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
         arr[left],arr[right] = arr[right],arr[left]
      
      if arr[left] <= arr[pivot]:
         left+=1
      
      if arr[right] >= arr[pivot]:
         right -= 1

   arr[pivot],arr[right] = arr[right],arr[pivot]

   qshelper(arr,start,right-1)
   qshelper(arr,right+1,end)

   

print(quickSOrt([5,3,8,4,1,0,7]))

"""
Time Complexity
Worst case = O(n^2)
Best case = O(n(log(n)))
Avg case = O(n(log(n)))

Space Complexity = O(log(n))
"""