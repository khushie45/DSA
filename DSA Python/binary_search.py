def binarysearch(arr,x):
    l,r = 0,len(arr)
    
    while l<=r:
        mid = (l+r)//2
        if x > arr[mid]:
            l = mid + 1
        elif x < arr[mid]:
            r = mid - 1
        else:
            return mid
    return -1        
            
#binary search is applicable for sorted array only.
arr = [12,34,56,67,78,89,92,95]
x = int(input("Enter x:"))

print("Element",x,"is found at index",binarysearch(arr,x))

#index -1 means element not found.
#time complexity of binary search is O(log(n))
#Binary Search is an incredible algorithm to use on large, sorted arrays, or whenever we plan to search for elements repeatedly in a single array.
