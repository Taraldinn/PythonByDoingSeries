# Advance sets operations

friends = {"rolf", "ruth", "charlie"} 
guests = {"Jose", "bob", "rolf",  "michael"}


not_in_both = guests.symmetric_difference(friends)

print(not_in_both)


# Symmentic difference is the opposite of intersection


print(guests.difference(friends))

# difference is the opposite of intersection

print(friends.intersection(guests))

# intersection is used for taking common values 