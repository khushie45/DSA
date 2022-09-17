def swap(a,b,arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot = elements[start]
    i = start 
    j = end

    while i<j:
        while elements[i] < pivot:
            i += 1
        
        while elements[j] > pivot:
            j -= 1
        
        if i >= j:
            return j #when i and j cross each other
        
        swap(i,j,elements) #can also use elements[i], elements[j] = elements[j], elements[i]
    
def quick_sort(elements, start, end):
    if start<end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1) #left-partition
        quick_sort(elements, pi + 1, end) #right-partition
    
if __name__ == '__main__':
    elements = [11,9,29,8,3,15,28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
    
'''Time complexity:
average-case : O(nlogn)
worst-case : O(n2) when the array is already sorted
Space complexity: O(logn) auxiliary'''
