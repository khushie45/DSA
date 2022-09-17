def bubble_sort(arr):
    size = len(arr)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
                if arr[j+1] < arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
        if not swapped:
            break #this is helpful when the array is already sorted. More effecient way
                
if __name__ == '__main__':
    arr = [12,5,30,21,6,52]
    bubble_sort(arr)
    print(arr)
    
#time complexity : O(n2)
