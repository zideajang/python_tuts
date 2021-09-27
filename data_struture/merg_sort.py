def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    # left = merge_sort(left)
    # right = merge_sort(right)
    merge_sort(left)
    merge_sort(right)

    return merge_two_sorted_lists(left,right,arr)



def merge_two_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        # print(b[j])
        # print(j)
        # print(i)
        print(a[i] <= b[j],j)
        if a[i] <= b[j]:
            arr[k] = a[i]
            sorted_list.append(a[i])
            i += 1
        else:
            arr[k] = b[j]
            sorted_list.append(b[j])
            j += 1
            print(j)
        k+=1
    # while i < len_a:
    #     sorted_list.append(a[i])
    #     arr[k] = a[i]
    #     i += 1
    #     k += 1
    # while j < len_b:
    #     arr[k] = b[j]
    #     sorted_list.append(b[j])
    #     j += 1
    #     k += 1

    return sorted_list

if __name__ == '__main__':
    a = [5,8,12,56]
    b = [7,9,45,51]

    arr = [5,8,12,56,7,9,45,51]
    # merge_sort(arr)
    print(merge_two_sorted_lists(a,b))