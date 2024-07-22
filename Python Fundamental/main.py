
friends = ["Rolf","Ruth","Charlie","jen"]
guests = ["Bob", "Jose" , "Rolf", "Charlie", "Micheal"]

counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1


print("------------------------------------------------------------------------------------")

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)

print("------------------------------------------------------------------------------------")

print(list(enumerate(friends)))
