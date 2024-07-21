numbers = [0, 1, 2, 3, 4]

double_numbers = []

for number in numbers:
    double_numbers.append(number * number)

print(double_numbers)


double_numbers = [ number * 3 for number in range(6) ]
print(double_numbers)


friend_ages = [22,31,35,37]

age_strings= [f"My Friends is {age} years old" for age in friend_ages]
print(age_strings)

names = ["Rolf", "Bob", "Jen"]

lower = [name.lower() for name in names]
print(lower)


