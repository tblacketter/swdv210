#!/usr/bin/env/python3

import db
from objects import Movie

def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("min - Dispaly movies under a certain number of minutes")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()

def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
    
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:        
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(name + " was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    choice = input(f"Are you sure you want to delete \'{db.get_movie(movie_id)}\'? (y/n): ")
    if choice == "y":
        db.delete_movie(movie_id)
    else:
        pass

def display_movies_by_minutes():
    minutes = get_int()
    movies = db.get_movies_by_minutes(minutes)
    print()
    display_movies(movies, f"LESS THAN {minutes} MINUTES")


def get_int()->int:
    while True:
        try:
            minutes = int(input("Maximum number of minutes: "))
            break
        except:
            print("Please enter an integer value")
    return minutes
 
def main():
    db.connect()
    display_title()
    display_categories()
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "min":
            display_movies_by_minutes()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
