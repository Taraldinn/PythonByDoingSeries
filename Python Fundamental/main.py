
friends = ["Rolf","Ruth","Charlie","jen"]
guests = ["Bob", "Jose" , "Rolf", "Charlie", "Micheal"]


time_since_seen = [3, 7, 15, 11]


# long_timers = {
#     friends[i]: time_since_seen[i]
#     for i in range(len(friends))
#
# }
#
# print(long_timers)


long_timers = dict(zip(friends, time_since_seen))
print(long_timers)

