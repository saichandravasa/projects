# storing 1000 995 990 .... 10 5 0 in a tuple
numbers = tuple(range(1000,-1,-5))

# printing first 5 elements
print(numbers[0:5])

# printing 0th element to 10th element
print(numbers[0:10])

# changing 0th element value to half of it self
numbers_list = list(numbers)
numbers_list[0] = numbers_list[0] // 2
numbers = tuple(numbers_list)
print(numbers)
