


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
"""
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
    def __getitem__(self,i):
        return self.cars[i]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        return f'Garage with {len(self)} cars'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford)

"""
class Employee:
    name = "Rolf"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
# e = Employee
# print(len(e))  # 4
# print(len(e))  # 4


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __str__(self):
        return f"{self.name} with id: {self.id}"

s1 = Student("John", 101)
s2 = Student("Jane", 102)
print(s1)