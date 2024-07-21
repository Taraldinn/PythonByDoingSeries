numbers = [0, 1, 2, 3, 4]

double_numbers = []

for number in numbers:
    double_numbers.append(number * number)

print(double_numbers)


double_numbers = [ number * 3 for number in range(6) ]
print(double_numbers)