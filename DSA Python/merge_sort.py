def merge_sort(arr):
    if len(arr) <= 1:
        return 
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge_two_sorted_lists(left,right,arr)
    
def merge_two_sorted_lists(a,b,arr):
    i = j = k = 0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
        
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
        
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1   
        
if __name__ == '__main__':
    arr = [10,3,15,7,9,87,26]
    print("Before sorting :",arr)
    merge_sort(arr)
    print("After sorting :",arr)
    
'''Time Complexity:
Best Case: O(n*log n)
Worst Case: O(n*log n)
Average Case: O(n*log n)

Space Complexity: O(n) '''
