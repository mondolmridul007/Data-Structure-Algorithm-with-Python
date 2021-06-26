
def counting_sort(arr, d):
 
    n = len(arr)

    sorted_array = [0 for _ in range(n)]

    count = [0 for _ in range(10)]

    for i in range(0, n):
        index = (arr[i] / d)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / d)
        sorted_array[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = sorted_array[i]

def radix_sort(arr):
 
    max_element = max(arr)
    exponential = 1
    while max_element / exponential > 0:
        counting_sort(arr, exponential)
        exponential *= 10
    return arr

with open('input.txt') as f:
    array = [int(x) for x in next(f).split()]

sorted = str(radix_sort(array))

f = open("output.txt","w")
f.write(sorted)
