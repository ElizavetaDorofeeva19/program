from functools import reduce

def square_numbers(numbers: list):
    return list(map(lambda x: x ** 2, numbers))
input_data = [1, 2, 3, 4, 5]
result =  square_numbers(input_data)
print(result) # [1, 4, 9, 16, 25]

def filter_even_numbers(numbers: list):
    return list(filter(lambda x: x % 2 == 0, numbers))
input_data = [1, 2, 3, 4, 5, 6]
result = filter_even_numbers(input_data)
print(result) # [2, 4, 6]


def multiply_numbers(numbers: list):
    return reduce(lambda x, y: x * y, numbers)
input_data = [1, 2, 3, 4]
result = multiply_numbers(input_data)
print(result) # 24

def sum_of_squares_of_even_numbers(numbers: list) :
    numbers = filter(lambda x: x % 2 == 0, numbers)
    numbers = list(map(lambda x: x ** 2, numbers))
    return reduce(lambda x, y: x + y, numbers)
input_data = [1, 2, 3, 4, 5]
result = sum_of_squares_of_even_numbers(input_data)
print(result) # 20 (2^2 + 4^2)

def word_length_map(input_string):
    dictionary = dict()
    a = any(map(lambda s: dictionary.update({s: len(s)}), input_string.split()))
    return dictionary
input_data = "hello world this is Python"
result = word_length_map(input_data)
print(result)


