NAME = "Merge Sort"

def merge_sort(sorting, low, high):
    if low < high:
        mid = (low + high) // 2

        # Recursively sort the left and right halves
        merge_sort(sorting, low, mid)
        merge_sort(sorting, mid + 1, high)

        # Merge the sorted halves
        return merge(sorting, low, mid, high)
    return 0

def merge(sorting, low, mid, high):
    left_half = sorting.arr[low:mid + 1]
    right_half = sorting.arr[mid + 1:high + 1]

    i = j = 0
    k = low 

    while i < len(left_half) and j < len(right_half):
        # Check if user wants to go back home
        check = sorting.event_check()
        if check == 3000:
            return 1
        if left_half[i] <= right_half[j]:
            sorting.arr[k] = left_half[i]
            i += 1
        else:
            sorting.arr[k] = right_half[j]
            j += 1
        sorting.update(k, NAME)
        k += 1

    # Copy the remaining elements of left_half, if any
    while i < len(left_half):
        check = sorting.event_check()
        if check == 3000:
            return 1
        sorting.arr[k] = left_half[i]
        sorting.update(k, NAME)
        i += 1
        k += 1

    # Copy the remaining elements of right_half, if any
    while j < len(right_half):
        check = sorting.event_check()
        if check == 3000:
            return 1
        sorting.arr[k] = right_half[j]
        sorting.update(k, NAME)
        j += 1
        k += 1
    return 0