def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while(True):
        i += 1
        while (arr[i] < pivot):
            i += 1
        j -= 1
        while (arr[j] > pivot):
            j -= 1
        if( i >= j):
            return j
        arr[i], arr[j] = arr[j],arr[i]

def lumuto_partition(arr, low, high):
    pivot = arr[high]

    i = (low -1)
    for j in range(low,high):
        if (arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j],arr[i]
    arr[i + 1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if (low < high):
        pi = hoare_partition(arr,low,high)

        quickSort(arr,low, pi)
        quickSort(arr, pi+1, high)

arr = [9, 21, 29, 38, 4, 17, 11, 25, 32]
quickSort(arr,0,len(arr)-1)
print(arr)