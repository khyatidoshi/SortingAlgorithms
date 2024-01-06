def selectionSort(arr):
    n = len(arr)
    for i in range(0,n-1): # n-1 because we don't need to sort the last element
        minimum_value_index = i 
        for j in range(i+1,n):
            if arr[j] < arr[minimum_value_index]:
                minimum_value_index = j 
        tmp = arr[i]
        arr[i] = arr[minimum_value_index]
        arr[minimum_value_index] = tmp
    return arr
