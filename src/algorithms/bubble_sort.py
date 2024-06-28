NAME = "Bubble Sort"

def bubble_sort(sorting):
    n = len(sorting.arr)
    for i in range(n):
        # Flag to optimize if no swaps are made in a pass
        swapped = False

        # Perform a single pass of bubble sort
        for j in range(0, n - i - 1):
            # Check if user wants to go back home
            check = sorting.event_check()
            if check == 3000:
                return 1

            # Swap if the element found is greater than the next element
            if sorting.arr[j] > sorting.arr[j + 1]:
                sorting.arr[j], sorting.arr[j + 1] = sorting.arr[j + 1], sorting.arr[j]
                sorting.update(j, NAME)
                sorting.update(j + 1, NAME)
                swapped = True

        # If no elements were swapped in this pass, array is already sorted
        if not swapped:
            break
    return 0