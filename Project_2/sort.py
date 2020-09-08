# from recursioncounter import RecursionCounter
from time import perf_counter
import random



def quicksort(lyst):
    # Use recursion
    pass


def quicksort_helper(low, high, lyst):
    pass


def mergesort(lyst):
    # Use recursion
    pass


def mergesort_helper(low, high, lyst):
    pass


def insertion_sort(lyst):
    pass


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


def randarray():
    """ Creates an array of random integers and assigns it to seed(2). """
    DATA_SIZE = 10
    random.seed(2)  # saves the generated list to seed(2)
    return random.sample(range(100), k=DATA_SIZE)


def main():
    test_array = [7, 11, 10, 46, 21, 94, 85, 39, 32, 77]
    # print('SELECTION SORT: ', selection_sort(randarray()))






    # selection sort
    print('starting selection sort)
    selection_sort_start = perf_counter()
    selection_sort(randarray())
    selection_sort_stop = perf_counter()
    selection_sort_time = selection_sort_stop - selection_sort_start
    print(f'{"%.10f"%selection_sort_time} seconds. \n')

    # timsort
    print('starting timsort')
    timsort_start = perf_counter()
    timsort(randarray())
    timsort_end = perf_counter()
    timsort_time = timsort_end - timsort_start
    print(f'{"%.10f"%timsort_time} seconds. \n')

    # print('UNSORTED RANDARRAY: ', randarray())


main()


""" Each function should """
# verify that the parameter is a list
# assume the list only contains integers
# assume the list is randomized
# each function should return a sorted list
# must use built in timsort --> dont write yourself
# use the recursive counter function for quicksort and mergesort


""" Checklist """
# quick sort                             []
# mergesort                              []
# insertion sort                         []
# selection sort                         [DONE] https://www.educative.io/edpresso/how-to-implement-selection-sort-in-python
# random array                           [DONE]
# timing for all functions               [IN PROGRESS]
# main                                   []
# timing results are 2 are 2 sigfigs     []
# use large array size (10,000 - 50,000) []
# built in timsort                       [DONE] https://realpython.com/sorting-algorithms-python/#implementing-timsort-in-pytho


""" Other """
# make sure that the lyst is randomized after every function            [FIXED] use randarray()
# remove the return statement of each function when doen                []


