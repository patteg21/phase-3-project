from models import Author, Book

print("""
Hello there and Welcome to my application

COMMANDS (case insensitive)
---------------------------------------------------------------
Add Author: 'a'
Add Book: 'b'
List of Authors: 'l'

Exit: 'x' 
---------------------------------------------------------------
""")

response = input().lower()

while response != "x":

    if response == "a":
        
        name = input("Name: ")
        
        new_author = Author(name=name)


    elif response == "b":
        print("b")
    elif response == "l":
        print("l")



    response = input("").lower()