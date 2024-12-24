from os import system
system('clear')
import random


#   Series 14
def find_small(k, numbers):
    return len([i for i in numbers if i < k])

#print(find_small(120, [10, 30, 200, 230, 60, 590]))
#print(find_small(120, [1000, 300, 200, 230, 600, 590]))


#   Series 15

def first_greater(k: int, numbers: list ):
    return min([numbers.index(x) for x in numbers if x > k])

# print(first_greater(120, [10, 30, 200, 230, 60, 590]))
# print(first_greater(120, [1000, 300, 200, 230, 600, 590]))


#   Series 16
def last_greater(k: int, numbers: list):
    return max([numbers.index(i) for i in numbers if i > k])

# print(last_greater(120, [10, 30, 200, 230, 60, 590]))
# print(last_greater(120, [1000, 300, 200, 230, 600, 590]))


#   Series 17

def dont_understand(b, n):
    return f'{str(b)} '.join(map(str, [random.randint(0, 1000) for _ in range(n)])) + str(b)

# print(dont_understand(77, 5))


#   Series 18

def do_something(n: int):
    return sorted(set([int(input("Enter Number: ")) for _ in range(n)]))

# print(do_something(4))


#   Series 19

def greater_than_left(n):
    my_lst = [random.randint(0, 1000) for _ in range(n)]
    result = [val for val in my_lst[1:] if val < my_lst[my_lst.index(val) - 1]]
    print(my_lst)
    return result, len(result)

print(greater_than_left(4))