def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index+1, size):
            if elements[j] < elements[min_index]:
                min_index = j
        if i != min_index:
            arr[i],arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':  
    elements = [11,5,2,23,45,31]
    
    selection_sort(elements)
    print(elements)
    
#time complexity : O(n2)
