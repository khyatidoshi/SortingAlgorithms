def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        x = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > x:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = x
                break
    return arr 
