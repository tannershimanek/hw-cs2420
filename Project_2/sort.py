def selection_sort(lyst):
    i = 0
    while i < len(lyst) - 1:            # Do n-1 searches
        minIndex = i                    # for the smallest
        j = i + 1
        while j < len(lyst):            # Start a search
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:               # Exchange if needed
            swap(lyst, minIndex, i)
        i += 1

