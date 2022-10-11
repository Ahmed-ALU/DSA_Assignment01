import random

list_of_nums = list()
list_length = int(20)

# Generate random list
for i in range(random.randint(2, list_length)):
    list_of_nums.append(random.randint(1, 100))

k = random.randint(2, len(list_of_nums))


def Question02(nums_list, n):
    # Indicating Variables
    counter = int(0)
    sum = int()
    # The main Algoritm
    list_of_nums.sort(reverse=True)
    for i in range(k):
        sum += int(list_of_nums[counter])
        counter +=1

    print(f"The summition of the first {k} largest numbers in the list = {sum}")
    print(f"The list is {list_of_nums}")
    return sum, list_of_nums

Question02(list_of_nums, k)

