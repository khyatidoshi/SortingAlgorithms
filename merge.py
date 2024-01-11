def merge(arr, l, m, r):
    L = []
    R = []
 
    for i in range(0, m-l+1):
        L.append(arr[l + i])
 
    for j in range(0, r-m):
        R.append(arr[m + 1 +j])
  
    i = 0    
    j = 0   
    k = l 
 
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    
    return arr
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h 
        # especially in case when l+h is larger than the range of int
        m = l+(r-l)//2
 
        arr = mergeSort(arr, l, m)
        arr = mergeSort(arr, m+1, r)
        arr = merge(arr, l, m, r)
    return arr
