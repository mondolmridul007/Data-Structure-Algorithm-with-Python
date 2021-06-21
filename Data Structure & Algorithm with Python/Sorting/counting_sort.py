def counting_sort(arr):
    #Example: 3 6 4 1 3 4 1 4
    p = max(arr) + 1
    #countpos & countfreq array length should be max(arr) + 1
    sorted_array = [0 for _ in range(len(arr))]
    #[0, 0, 0, 0, 0, 0, 0, 0]

    countpos = [0 for _ in range(p)]
    #To find how many times an element occurs
    for x in arr:
        countpos[x]+=1
    #Example: [0, 2, 0, 2, 3, 0, 1]
    countfreq = [0 for _ in range(p)]
    #to find the exect position where the arr element to be put in sorted array
    for x in range(1,p):
        countfreq[x] = countfreq[x-1] + countpos[x]
    #Example: [0, 2, 2, 4, 7, 7, 8]

    for i in range(len(arr)):
        freq_index_value = countfreq[arr[i]] #4 for first
        sorted_array[freq_index_value - 1] = arr[i] #3 is put on 3rd position in sorted array for first
        countfreq[arr[i]]-=1 #decresing value of countfreq sothat the same element can be put before the element
    print(sorted_array)
    #Example: [1, 1, 3, 3, 4, 4, 4, 6]

array = list(map(int, input().rstrip().split()))
counting_sort(array)

#pseudocode link: https://www.codingeek.com/algorithms/counting-sort-explanation-pseudocode-and-implementation/
#Explaination link: https://www.youtube.com/watch?v=wP_GoeEPB1w
