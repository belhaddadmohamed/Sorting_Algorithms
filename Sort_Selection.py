def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


print(selection_sort([1,8,2,3,5,1,2]))
