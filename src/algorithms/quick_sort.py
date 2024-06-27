def partition(sorting, low, high):
    i = (low - 1)
    pivot = sorting.arr[high] 
    for j in range(low , high):
        sorting.event_check()
        if(sorting.arr[j] < pivot): 
            i = i + 1 
            sorting.arr[i], sorting.arr[j] = sorting.arr[j], sorting.arr[i]
            sorting.update(j, "Quick Sort")
            sorting.update(i, "Quick Sort")
            check = sorting.event_check()
            if check == 3000:
                return check
    sorting.arr[i + 1], sorting.arr[high] = sorting.arr[high], sorting.arr[i + 1]
    sorting.update(high,"Quick Sort")
    sorting.update(i + 1, "Quick Sort")
    check = sorting.event_check()
    if check == 3000:
        return check
    return i + 1

def quick_sort(sorting, low, high): 
    if low < high:
        pi = partition(sorting, low, high)
        if pi == 3000:
            return 1
        quick_sort(sorting, low, pi - 1) 
        quick_sort(sorting, pi + 1, high)
    return 0
