def swap(a,b,arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        i+=1
        while arr[i]<pivot:
            i += 1
        
        j-=1
        while arr[j]>pivot:
            j -= 1
        
        if i>=j: #when two pointers meet or cross each other
            return j
        
        swap(i,j,arr) #can also write arr[i], arr[j] = arr[j], arr[i]
    
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high) #pi is the partitioning index
        quick_sort(arr, low, pi) #left-partition
        quick_sort(arr, pi+1, high) #right-partition
    
if __name__ == '__main__':
    elements = [11,9,29,8,3,15,28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
    
'''Time complexity:
average-case : O(nlogn)
worst-case : O(n2) when the array is already sorted
Space complexity: O(logn) auxiliary'''
