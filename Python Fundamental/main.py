


# class Movie:
#     def __init__(self, title, director, year):
#         self.title = title
#         self.director = director
#         self.year = year

#     def print_info(self):
#         print(f'{self.title} by {self.director} in {self.year}')


# friends = LockableList("Rolf", "Bob", "Jen")
# friends.append("Adam")
# print(friends)  # ['Rolf', 'Bob', 'Jen', 'Adam']

# friends.lock()
# friends.append("Anne")  # Error


# class LockableList(list):
#     def __init__(self,values,locked=False):
#         self.values = list(values)
#         self._locked = locked

# locks = LockableList([1,2,3])
# print(locks.values)  # [1, 2, 3]
# print(locks._locked)  # False

class Student:
    def __init__(self,name):
        self.name = name

movies = ['Matrix','Finding Nemo']
print(movies.__class__)
print(len(movies))


class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(len(ford))