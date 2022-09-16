def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i] #anchor is the pointer 
        j = i - 1
        while j >=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
         
if __name__ == '__main__':
    elements = [11,9,29,7,3,17,27]
    insertion_sort(elements)
    print(elements)
    
''' Time complexities :
Worst-case : O(n2) comparisions and swaps
Best-case : O(n) comparisions, O(1) swaps
Average-case : O(n2) comparisions and swaps
Worst-case space complexity: O(n) total, O(1) auxiliary space '''
