def insersionSort(arr):
   for i in range(1,len(arr)):
      key = arr[i]
      last = i-1

      while last >= 0 and key < arr[last]:
         arr[last + 1] = arr[last]
         last-=1

      arr[last + 1] = key
   
   return arr

print(insersionSort([4,2,47,1,5,7,4]))


"""
Time Complexity
Worst case = O(n^2)
Best case = O(n)
Avg case = O(n^2)

Space Complexity = O(1)
"""