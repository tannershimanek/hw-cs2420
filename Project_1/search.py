from recursioncounter import RecursionCounter
from time import perf_counter
import random
import math

binary_search_checker = True
ValueError_checker = False


def linear_search(lyst, target):
    if type(target) == int:
        for index in lyst:
            try:
                i = int(index)
            except ValueError:
                print(
                    '\tValueError: One or more non integer values could not be converted. MAKE SURE TO ONLY USE INTEGERS.')
            finally:
                if i == target:
                    return True
        return False
    else:
        print("\tlinear_search() test FAILED. Target value is not an integer.")


def recursive_binary_search(lyst, target):
    global ValueError_checker
    if type(target) == int:
        for index in lyst:
            try:
                index = int(index)
            except ValueError:
                ValueError_checker = True
                print(
                    '\tValueError: One or more non integer values could not be converted. MAKE SURE TO ONLY USE INTEGERS.')

        if ValueError_checker is False:
            low_index = 0
            high_index = len(lyst)
            recursive_binary_search_helper(lyst, low_index, high_index, target)
            if binary_search_checker is True:
                return True
            else:
                return False
        else:
            return False
    else:
        print("\trecursive_binary_search() test FAILED. Target value is not an integer.")


def recursive_binary_search_helper(lyst, low_index, high_index, target):
    RecursionCounter()
    global binary_search_checker
    if target <= lyst[-1]:
        if high_index >= low_index:
            mid = (high_index + low_index) // 2
            if lyst[mid] == target:
                binary_search_checker = True
            elif lyst[mid] > target:
                recursive_binary_search_helper(
                    lyst, low_index, mid - 1, target)
            else:
                recursive_binary_search_helper(
                    lyst, mid + 1, high_index, target)
        else:
            binary_search_checker = False
    else:
        binary_search_checker = False


def jump_search(lyst, target):
    global ValueError_checker
    if type(target) == int:
        for index in lyst:
            try:
                index = int(index)
            except ValueError:
                ValueError_checker = True
                print(
                    '\tValueError: One or more non integer values could not be converted. MAKE SURE TO ONLY USE INTEGERS.')

        if ValueError_checker == False:
            length = len(lyst)
            step = math.sqrt(length)

            prev = 0
            while lyst[int(min(step, length) - 1)] < target:
                prev = step
                step += math.sqrt(length)

                if int(prev) >= length:
                    return False

            while lyst[int(prev)] <= target:
                if lyst[int(prev)] == target:
                    return True

                prev += 1
                if int(prev) == int(min(step, length)):
                    return False

                if lyst[int(prev)] == target:
                    return True
        else:
            return False
    else:
        print('jump_search() test FAILED. Target value is not an integer.')


def randarray():
    """Creates an array of random integers and assigns it to seed(1)."""
    random.seed(1)  # saves the generated list to seed(1)
    return sorted(random.sample(range(10000000), k=60000))


def main():
    global ValueError_checker
    target_start = 3719  # Edit values here.
    target_mid = 5669005
    target_end = 9999393

    # start of array
    print('Searching for a number at the start of the array..')

    linear_search_time_start_1 = perf_counter()
    linear_search_start_of_array = linear_search(randarray(), target_start)
    linear_search_time_stop_1 = perf_counter()
    linear_search_time_1 = linear_search_time_stop_1 - linear_search_time_start_1
    print(
        f'\tlinear_search() returned {linear_search_start_of_array} in {"%.10f"%linear_search_time_1} seconds')

    ValueError_checker = False
    recursive_binary_search_time_start_1 = perf_counter()
    recursive_binary_search_start_of_array = recursive_binary_search(
        randarray(), target_start)
    recursive_binary_search_time_stop_1 = perf_counter()
    recursive_binary_search_time_1 = recursive_binary_search_time_stop_1 - \
        recursive_binary_search_time_start_1
    print(
        f'\trecursive_binary_search() returned {recursive_binary_search_start_of_array} in {"%.10f"%recursive_binary_search_time_1} seconds')

    ValueError_checker = False
    jump_search_time_start_1 = perf_counter()
    jump_search_start_of_array = jump_search(randarray(), target_start)
    jump_search_time_stop_1 = perf_counter()
    jump_search_time_1 = jump_search_time_stop_1 - jump_search_time_start_1
    print(
        f'\tjump_search() returned {jump_search_start_of_array} in {"%.10f"%jump_search_time_1} seconds')

    # middle of array
    print('Searching for a number in the middle of the array..')

    linear_search_time_start_2 = perf_counter()
    linear_search_start_of_array = linear_search(randarray(), target_mid)
    linear_search_time_stop_2 = perf_counter()
    linear_search_time_2 = linear_search_time_stop_2 - linear_search_time_start_2
    print(
        f'\tlinear_search() returned {linear_search_start_of_array} in {"%.10f"%linear_search_time_2} seconds')

    ValueError_checker = False
    recursive_binary_search_time_start_2 = perf_counter()
    recursive_binary_search_start_of_array = recursive_binary_search(
        randarray(), target_mid)
    recursive_binary_search_time_stop_2 = perf_counter()
    recursive_binary_search_time_2 = recursive_binary_search_time_stop_2 - \
        recursive_binary_search_time_start_2
    print(
        f'\trecursive_binary_search() returned {recursive_binary_search_start_of_array} in {"%.10f"%recursive_binary_search_time_2} seconds')

    ValueError_checker = False
    jump_search_time_start_2 = perf_counter()
    jump_search_start_of_array = jump_search(randarray(), target_mid)
    jump_search_time_stop_2 = perf_counter()
    jump_search_time_2 = jump_search_time_stop_2 - jump_search_time_start_2
    print(
        f'\tjump_search() returned {jump_search_start_of_array} in {"%.10f"%jump_search_time_2} seconds')

    # end of array
    print('Searching for a number at the end of the array..')
    linear_search_time_start_3 = perf_counter()
    linear_search_start_of_array = linear_search(randarray(), target_end)
    linear_search_time_stop_3 = perf_counter()
    linear_search_time_3 = linear_search_time_stop_3 - linear_search_time_start_3
    print(
        f'\tlinear_search() returned {linear_search_start_of_array} in {"%.10f"%linear_search_time_3} seconds')

    ValueError_checker = False
    recursive_binary_search_time_start_3 = perf_counter()
    recursive_binary_search_start_of_array = recursive_binary_search(
        randarray(), target_end)
    recursive_binary_search_time_stop_3 = perf_counter()
    recursive_binary_search_time_3 = recursive_binary_search_time_stop_3 - \
        recursive_binary_search_time_start_3
    print(
        f'\trecursive_binary_search() returned {recursive_binary_search_start_of_array} in {"%.10f"%recursive_binary_search_time_3} seconds')

    ValueError_checker = False
    jump_search_time_start_3 = perf_counter()
    jump_search_start_of_array = jump_search(randarray(), target_end)
    jump_search_time_stop_3 = perf_counter()
    jump_search_time_3 = jump_search_time_stop_3 - jump_search_time_start_3
    print(
        f'\tjump_search() returned {jump_search_start_of_array} in {"%.10f"%jump_search_time_3} seconds')

    # use this to find info on your random array
    # print(randarray()) 


main()
