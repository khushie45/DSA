def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [12,52,34,64,88,21]
x = int(input("Enter x: "))

print("Element",x,"is present at index",linear_search(arr,x))

#time complexity of linear search is O(n)
