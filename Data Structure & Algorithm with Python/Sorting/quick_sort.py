def partition(arr, i, j):

    pivot_index = i
    pivot = arr[pivot_index]
    while i<j:
        while i < len(arr) and arr[i] <= pivot:
            i+=1
        while arr[j] > pivot:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

        arr[pivot_index], arr[j] = arr[j], arr[pivot_index]

    return j

def quick_sort(arr, beg, end):

    if beg<end:
        p = partition(arr,beg, end)
        quick_sort(arr, beg, p-1)
        quick_sort(arr, p + 1, end)


array = list(map(int, input().rstrip().split()))
low = 0
high = len(array) - 1
quick_sort(array, low, high)
print(f'Sorted array: {array}')

#Resource- https://www.geeksforgeeks.org/quick-sort/
#Explanation- https://www.youtube.com/watch?v=7h1s2SojIRw&t=518s
