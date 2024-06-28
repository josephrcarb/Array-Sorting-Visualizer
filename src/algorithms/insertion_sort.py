NAME = "Insertion Sort"

def insertion_sort(sorting): 
    for i in range(1, len(sorting.arr)):
        check = sorting.event_check()

        if(check == 3000):
            return 100
        if(check == 5000):
            return 1
        
        key = sorting.arr[i] 
        j = i - 1

        while j >= 0 and key < sorting.arr[j] : 
                sorting.arr[j + 1] = sorting.arr[j]
                j = j - 1
                sorting.update(j + 1, NAME) 
                check = sorting.event_check()
                if check == 3000:
                    return 1

        sorting.arr[j + 1] = key
        sorting.update(j + 1, NAME)
        check = sorting.event_check()
        if check == 3000:
            return 1
    return 0
