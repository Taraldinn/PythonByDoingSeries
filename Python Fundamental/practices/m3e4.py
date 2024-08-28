class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def print_info(self):
        print(f'{self.title} by {self.director} in {self.year}')



movie = Movie('The Matrix', 'Wachowski', 1994)
movie.print_info()
