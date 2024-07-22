ages = [22,35,27,21,20]

odds = [age for age in ages if age % 2 == 1  ]
print(odds)


friends = ["Rolf","Ruth","Charlie","jen"]
guests = ["Bob", "Jose" , "Rolf", "Charlie", "Micheal"]

friends_lower = set({f.lower() for f in friends})
guest_lower = set({g.lower() for g in guests})

print(friends_lower.intersection(guest_lower))

present_friends = [
    name.title() for name in guests if name.lower() in friends
]
print(present_friends)