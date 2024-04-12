# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n // x)
#             break

# FizzBuzz Problem Solving
"""
if result dividabel by 3 is fizz or if result dividable by 5 is buzz
if result dividable by 3 and 5 is fizzbuzz

"""

# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# double_numbers = []

# for number in number:
#     double_numbers.append(number * 2)
# print(double_numbers)

# double_numbers = [number * 2 for number in numbers]
# print(double_numbers)

friends = ["rolf", "ruth", "charlie", "jen"]
guests = ["Jose", "bob", "rolf", "charli", "michael"]

friends_lower = set([n.lower() for n in friends])
guests_lower = set([n.lower() for n in guests])

print(friends_lower.intersection(guests_lower))
