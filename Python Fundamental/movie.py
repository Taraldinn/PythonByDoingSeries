# add new movie
# get movie list
# find movie
from main import add_movie, movies, print_movie

promt = 'Enter "a" to add a movie, "l" to see your movies, "f" to find a movie, and "q" to quit: '

movies = []


def add_movie():
    title = input("Your Movie Title")
    director = input("Director Name")
    year = input("Released Year")

    movies.append({
        'title' : title,
        'director' : director,
        'year' : year 
    })


def show_movies():
    for movie in movies:
        print_movie(movie)

        def print_movie():
                print(f"Title: {movie['title']}")
                print(f"Director: {movie['director']}")
                print(f"Release Year: {movie['year']}")

def find_movie():
    search_title = input("Search with title")
        
    for movie in movies:
        if movie['title'] == search_title:
            print(movie)

user_option = {
    "a" : add_movie,
    "l" : show_movies,
    "f" : find_movie,
}




def menu():
     menu = input(promt)

     while promt != "q":
          if promt in user_option:
               selected_function = user_option(promt)
               selected_function()
          else:
                print("Unknown commad plz try again")

               


"""
def menu():
    menu = input("")
    while menu != 'q':
        if menu == 'a':
            add_movie()
        elif menu == 'l':
            show_movies()
        elif menu == 'f':
            find_movie()
        else:
            print("Unknown commad plz try again")
        menu = input("Your promt")

"""