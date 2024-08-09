from itertools import combinations

nums = [1, 2, 3, 4]


def print_combinations(elements):
    total_length = len(elements)
    print(f"Total: {total_length}")
    for i in range(total_length + 1):
        print(f"count: {i}")
        for combination in combinations(nums, i):
            print(combination)


def return_list_of_combinations(elements):
    results_list = [()]
    for i in range(1, len(elements) + 1):
        results_list.extend(combinations(elements, i))

    return results_list


# def return_list_of_combinations(elements): # Another solution
#     results_list = [()]
#     for i in range(1, len(elements) + 1):
#         for combination in combinations(elements, i):
#             results_list.append(combination)
#
#     return results_list


print(return_list_of_combinations(nums))
