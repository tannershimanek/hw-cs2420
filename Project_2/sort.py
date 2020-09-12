from recursioncounter import RecursionCounter
from time import perf_counter
import random


def quicksort(lyst):
    try:
        if type(lyst) == list:
            try:
                if all(type(x) is int for x in lyst):
                    return quicksort_helper(lyst)
                else:
                    raise ValueError(
                        'ValueError: List contains 1 or more '
                        'non integer type values.\n')
            except ValueError as err:
                print(err)
                raise
        else:
            raise ValueError(
                'ValueError: Parameter is not a list.\n')
    except ValueError as err:
        print(err)
        raise


def quicksort_helper(lyst):
    """The recursive part of quicksort."""
    RecursionCounter()
    length_of_list = len(lyst)

    if length_of_list < 2:
        return lyst

    current_position = 0

    for i in range(1, length_of_list):
        if lyst[i] <= lyst[0]:
            current_position += 1
            temp = lyst[i]
            lyst[i] = lyst[current_position]
            lyst[current_position] = temp

    temp = lyst[0]
    lyst[0] = lyst[current_position]
    lyst[current_position] = temp

    left = quicksort_helper(lyst[0:current_position])
    right = quicksort_helper(lyst[current_position + 1:length_of_list])

    lyst = left + [lyst[current_position]] + right

    return lyst


def mergesort(lyst):
    try:
        if type(lyst) == list:
            try:
                if all(type(x) is int for x in lyst):
                    return mergesort_helper(lyst)
                elif all(type(x) is not int for x in lyst):
                    raise ValueError(
                        'ValueError: List contains 1 or more '
                        'non integer type values.\n')
            except ValueError as err:
                print(err)
                raise
        else:
            raise ValueError(
                'ValueError: Parameter is not a list.\n')
    except ValueError as err:
        print(err)
        raise


def mergesort_helper(lyst):
    """The recursive part of mergesort."""
    RecursionCounter()

    if len(lyst) > 1:
        mid = len(lyst) // 2
        left = lyst[:mid]
        right = lyst[mid:]

        mergesort_helper(left)
        mergesort_helper(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lyst[k] = left[i]
                i += 1
            else:
                lyst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lyst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lyst[k] = right[j]
            j += 1
            k += 1

    return lyst


def insertion_sort(lyst):
    try:
        if type(lyst) == list:
            try:
                if all(type(x) is int for x in lyst):
                    for i in range(1, len(lyst)):
                        key = lyst[i]
                        j = i - 1
                        while j >= 0 and lyst[j] > key:
                            lyst[j + 1] = lyst[j]
                            lyst[j] = key
                            j -= 1

                    return lyst
                else:
                    raise ValueError(
                        'ValueError: List contains 1 or more '
                        'non integer type values.\n')
            except ValueError as err:
                print(err)
                raise
        else:
            raise ValueError(
                'ValueError: Parameter is not a list.\n')
    except ValueError as err:
        print(err)
        raise


def selection_sort(lyst):
    try:
        if type(lyst) == list:
            try:
                if all(type(x) is int for x in lyst):
                    length_of_array = len(lyst)

                    for i in range(length_of_array):
                        minimum = i

                        for j in range(i+1, length_of_array):
                            if lyst[j] < lyst[minimum]:
                                minimum = j

                        temp = lyst[i]
                        lyst[i] = lyst[minimum]
                        lyst[minimum] = temp

                    return lyst
                else:
                    raise ValueError(
                        'ValueError: List contains 1 or more '
                        'non integer type values.\n')
            except ValueError as err:
                print(err)
                raise
        else:
            raise ValueError(
                'ValueError: Parameter is not a list.\n')
    except ValueError as err:
        print(err)
        raise


def timsort(lyst):
    try:
        if type(lyst) == list:
            try:
                if all(type(x) is int for x in lyst):
                    return sorted(lyst)
                else:
                    raise ValueError(
                        'ValueError: List contains 1 or more '
                        'non integer type values.\n')
            except ValueError as err:
                print(err)
                raise
        else:
            raise ValueError(
                'ValueError: Parameter is not a list.\n')
    except ValueError as err:
        print(err)
        raise


def is_sorted(lyst):
    """Checks if the list passed in is sorted and returns True or False."""
    try:
        if type(lyst) == list:
            try:
                if all(type(x) is int for x in lyst):
                    if all(lyst[i] <= lyst[i + 1] for i in range(len(lyst) - 1)):
                        return True
                    else:
                        return False
                else:
                    raise ValueError(
                        'ValueError: List contains 1 or more '
                        'non integer type values.\n')
            except ValueError as err:
                print(err)
                raise
        else:
            raise ValueError(
                'ValueError: Parameter is not a list.\n')
    except ValueError as err:
        print(err)
        raise


def main():
    DATA_SIZE = 10000  # change sample size
    random.seed(2)  # saves the generated list to seed(2)
    DATA = random.sample(range(50000), k=DATA_SIZE)

    # quick sort
    print('\nchecking if list is sorted..')
    if is_sorted(DATA.copy()) is False:
        print('starting quick sort...')
        quicksort_start = perf_counter()
        quicksort(DATA.copy())
        quicksort_stop = perf_counter()
        quicksort_time = quicksort_stop - quicksort_start
        print(f'quick sort duration {"%.10f"%quicksort_time} seconds.\n')
    elif is_sorted(DATA.copy()) is True:
        print('list sorted')

    # merge sort
    print('checking if list is sorted..')
    if is_sorted(DATA.copy()) is False:
        print('starting merge sort...')
        mergesort_start = perf_counter()
        mergesort(DATA.copy())
        mergesort_stop = perf_counter()
        mergesort_time = mergesort_stop - mergesort_start
        print(f'merge sort duration {"%.10f"%mergesort_time} seconds.\n')
    elif is_sorted(DATA.copy()) is True:
        print('list sorted')

    # insertion sort
    print('checking if list is sorted..')
    if is_sorted(DATA.copy()) is False:
        print('starting insertion sort...')
        insertion_sort_start = perf_counter()
        insertion_sort(DATA.copy())
        insertion_sort_stop = perf_counter()
        insertion_sort_time = insertion_sort_stop - insertion_sort_start
        print(
            'insertion sort duration '
            f'{"%.10f"%insertion_sort_time} seconds.\n')
    elif is_sorted(DATA.copy()) is True:
        print('List sorted')

    # selection sort
    print('checking if list is sorted..')
    if is_sorted(DATA.copy()) is False:
        print('starting selection sort...')
        selection_sort_start = perf_counter()
        selection_sort(DATA.copy())
        selection_sort_stop = perf_counter()
        selection_sort_time = selection_sort_stop - selection_sort_start
        print(
            'selection sort duration '
            f'{"%.10f"%selection_sort_time} seconds.\n')
    elif is_sorted(DATA.copy()) is True:
        print('List sorted')

    # timsort
    print('checking if list is sorted..')
    if is_sorted(DATA.copy()) is False:
        print('starting timsort...')
        timsort_start = perf_counter()
        timsort(DATA.copy())
        timsort_end = perf_counter()
        timsort_time = timsort_end - timsort_start
        print(f'timsort duration {"%.10f"%timsort_time} seconds.\n')
    elif is_sorted(DATA.copy()) is True:
        print('List sorted')


main()