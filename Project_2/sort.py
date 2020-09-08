from recursioncounter import RecursionCounter
from time import perf_counter
import random


is_list_sorted = False


def quicksort(lyst):
    # use recursion
    pass


def quicksort_helper(low, high, lyst):
    """ The recursive part of quicksort. """
    RecursionCounter() # needed for unit test
    pass


def mergesort(lyst):
    # use recursion
    pass


def mergesort_helper(low, high, lyst):
    """ The recursive part of mergesort. """
    RecursionCounter() # needed for unit test
    pass


def insertion_sort(lyst):
    for i in range(1, len(lyst)):
        key = lyst[i]

        j = i - 1
        while j >= 0 and lyst[j] > key:
            # swap
            lyst[j + 1] = lyst[j]
            lyst[j] = key

            # decrement j
            j -= 1

    return lyst


def selection_sort(lyst):
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


def timsort(lyst):
    return sorted(lyst)


def is_sorted(lyst):
    """ Checks if the list passed in is sorted. """
    global is_list_sorted

    if all(lyst[i] <= lyst[i + 1] for i in range(len(lyst) - 1)):
        is_list_sorted = True
    else:
        is_list_sorted = False


def main():
    DATA_SIZE = 10
    random.seed(2)  # saves the generated list to seed(2)
    DATA = random.sample(range(100), k=DATA_SIZE) # [7, 11, 10, 46, 21, 94, 85, 39, 32, 77]

    # quick sort




    # merge sort




    # insertion sort
    print('checking if list is sorted..')
    is_sorted(DATA.copy())
    if is_list_sorted == False:
        print('starting insertion sort...')
        insertion_sort_start = perf_counter()
        insertion_sort(DATA.copy())
        insertion_sort_stop = perf_counter()
        insertion_sort_time = insertion_sort_stop - insertion_sort_start
        print(f'insertion sort duration {"%.10f"%insertion_sort_time} seconds. \n')
    elif is_list_sorted == True:
        print('List sorted')

    # selection sort
    print('checking if list is sorted..')
    is_sorted(DATA.copy())
    if is_list_sorted == False:
        print('starting selection sort...')
        selection_sort_start = perf_counter()
        selection_sort(DATA.copy())
        selection_sort_stop = perf_counter()
        selection_sort_time = selection_sort_stop - selection_sort_start
        print(f'selection sort duration {"%.10f"%selection_sort_time} seconds. \n')
    elif is_list_sorted == True:
        print('List sorted')

    # timsort
    print('checking if list is sorted..')
    is_sorted(DATA.copy())
    if is_list_sorted == False:
        print('starting timsort...')
        timsort_start = perf_counter()
        timsort(DATA.copy())
        timsort_end = perf_counter()
        timsort_time = timsort_end - timsort_start
        print(f'timsort duration {"%.10f"%timsort_time} seconds. \n')
    elif is_list_sorted == True:
        print('List sorted')

    # print('UNSORTED RANDARRAY: ', DATA)


main()


""" Each function should """
# verify that the parameter is a list                               []
# assume the list only contains integers                            []
# assume the list is randomized                                     []
# each function should return a sorted list                         []
# must use built in timsort --> dont write yourself                 []
# use the recursive counter function for quicksort and mergesort    []


""" Checklist """
# quick sort                             []
# quick sort helper                      []
# mergesort                              []
# mergesort helper                       []
# insertion sort                         [DONE] https://www.educative.io/edpresso/how-to-implement-insertion-sort-in-python
# selection sort                         [DONE] https://www.educative.io/edpresso/how-to-implement-selection-sort-in-python
# random array                           [DONE]
# timing for all functions               [IN PROGRESS]
# main                                   [IN PROGRESS]
# timing results are 2 are 2 sigfigs     []
# use large array size (10,000 - 50,000) []
# built in timsort                       [DONE] https://realpython.com/sorting-algorithms-python/#implementing-timsort-in-pytho
# test is_sorted()                       [DONE]


""" Other """
# make sure that the lyst is randomized after every function            [FIXED] use DATA.copy()
# remove the return statement of each function when done                []
# meets coding stanadards (8.5+)                                        [IN PROGRESS]

