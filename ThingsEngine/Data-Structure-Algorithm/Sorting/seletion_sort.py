def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        minj = i

        for j in range(i+1, n):
            if arr[j] < arr[minj]:
                minj = j

        if minj != i:
            arr[i], arr[minj] = arr[minj], arr[i]

    return arr
