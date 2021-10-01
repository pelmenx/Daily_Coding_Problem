# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Oracle.
#
# We say a number is sparse if there are no adjacent ones in its binary
# representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a
# given input N, find the smallest sparse number greater than or equal to N.
#
# Do this in faster than O(N log N) time.
#
#
# --------------------------------------------------------------------------------
#
#
def find_smallest_sparse_number_greater_than_or_equal_to_n(n):
    bin_number_list = list(bin(n))[2:]
    first_pointer = -2
    last_pointer = -1
    save_ones = False
    while abs(last_pointer) < len(bin_number_list):
        if int(bin_number_list[first_pointer]) == 0 and save_ones:
            bin_number_list[first_pointer] = "1"
            save_ones = False
            first_pointer -= 1
            last_pointer -= 1
        if int(bin_number_list[last_pointer]) + int(bin_number_list[first_pointer]) == 0:
            first_pointer -= 2
            last_pointer -= 2
        elif int(bin_number_list[last_pointer]) + int(bin_number_list[first_pointer]) == 1:
            first_pointer -= 1
            last_pointer -= 1
        else:
            bin_number_list[last_pointer] = "0"
            bin_number_list[first_pointer] = "0"
            if abs(first_pointer) == len(bin_number_list):
                bin_number_list.insert(0, "1")
            else:
                if int(bin_number_list[first_pointer - 1]) == 0:
                    bin_number_list[first_pointer - 1] = "1"
                else:
                    save_ones = True
            first_pointer -= 2
            last_pointer -= 2
    return int(''.join(bin_number_list), 2)


assert find_smallest_sparse_number_greater_than_or_equal_to_n(21) == 21
assert find_smallest_sparse_number_greater_than_or_equal_to_n(22) == 32
assert find_smallest_sparse_number_greater_than_or_equal_to_n(255) == 256
