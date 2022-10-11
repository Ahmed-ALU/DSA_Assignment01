import pympler.asizeof as asz
import random

list_of_nums = list()

# Generate random list
for i in range(random.randint(2, 10)):
    list_of_nums.append(random.randint(1, 10))

def Question01(num_list) -> list:
    # Variables
    Unique_list_of_nums = list()
    counter = int()
    function_return = bool()

    """
    The Big O notation for the next Algorithm is O(2n) because we have 2 separated
    for loops and by considering the rule of droping constants it will be "O(n)"
    """

    # The main Algorithms
    for i in num_list:
        if i not in Unique_list_of_nums:
            Unique_list_of_nums.append(i)
        else:
            pass
    for i in range(len(Unique_list_of_nums)):
        if num_list.count(Unique_list_of_nums[counter]) % 2 == 0:
            function_return = False
        else:
            function_return = True
            break

    return num_list, function_return

size = asz.asizeof(print(Question01(list_of_nums)))
print(f"The szie taken by this algorithm is {size}")


