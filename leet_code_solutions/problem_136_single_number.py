from typing import List


def single_number(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num

    return res


def single_number_with_dict(nums: List[int]) -> int:
    dict_of_numbs = {}
    for num in nums:
        if num in dict_of_numbs:
            dict_of_numbs[num] += 1
        else:
            dict_of_numbs[num] = 1

    return list(filter(lambda x: dict_of_numbs[x] == 1, dict_of_numbs))[0]


print(single_number_with_dict([4, 1, 2, 1, 2, 4, 5, 5, 6]))
print(single_number([4, 1, 2, 1, 2, 4, 5, 5, 6]))

# Logical and Bitwise operators
# Logical And
# print(True and True)
# print(True and False)
#
# # Logical Or
# print(False or False)
# print(False or True)
#
# # ^
# print(True ^ True)
# print(False ^ False)
# print(False ^ True)
