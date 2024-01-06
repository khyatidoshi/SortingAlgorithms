def bubbleSort(arr):
    # print(" Array to Sort : ", arr)
    for i in range(0,len(arr)):
        swap = False
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                swap = True
                tmp=arr[j]
                arr[j] = arr[j+1]
                arr[j+1]=tmp
        # print("Pass",i," array = ", arr)
        if not swap:
            break
    return (arr)
