'''
Problem: Sorting in linear time: Counting Sort
1.Generate N random integers within range 0 to 10000 in a file named input.txt.
2.Implement bubble sort to sort the numbers (from input.txt) and count the time.
3.Implement counting sort to sort the numbers (from input.txt) and count the time.
'''

import time
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#    print(arr)


def counting_sort(arr):
    p = max(arr) + 1
    sorted_array = [0 for _ in range(len(arr))]

    countpos = [0 for _ in range(p)]
    for x in arr:
        countpos[x]+=1

    countfreq = [0 for _ in range(p)]

    for x in range(1,p):
        countfreq[x] = countfreq[x-1] + countpos[x]

    for i in range(len(arr)):
        freq_index_value = countfreq[arr[i]]
        sorted_array[freq_index_value - 1] = arr[i]
        countfreq[arr[i]]-=1
#    print(sorted_array)

import random
with open("input.txt", "w") as f:
    for i in range(5000):
        r = random.randint(0, 10000)
        f.write(str(r)+"\n")

array=[]
f1 = open('input.txt', 'r')
for line in f1.readlines():
    array.append(int(line))
    f1.close()

#For counter sort
start_counting = time.time()
counting_sort(array)
end_counting = time.time()
cst = end_counting - start_counting
print(f"Total time for Counting Sorting is {cst} seconds")

#For Bubble sort
start_bubble = time.time()
bubble_sort(array)
end_bubble = time.time()
bst = end_bubble - start_bubble
print(f"Total time for Bubble Sorting is {bst} seconds")