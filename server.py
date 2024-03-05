from models import Author, Book, Rating

# connect to my DB
try:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    print("\nDatabase connected... \n")
except:
    print ("\nDatabase not connected \n")

# Create Author table

def main():

    print("""
    Author and Book Tracker - CLI Application

    COMMANDS (case insensitive)
    ---------------------------------------------------------------
    Add Author: 'a'
    Find Authors Books: 'f'
    List of Authors: 'a -l'
    Add Book: 'b'
    Add Rating: 'b -r'
    List of Books: 'b -l'
    Remove Author: 'rm -a'
    Remove Book: 'rm -b'

    Cow: 'cow'

    Exit: 'x' 
    ---------------------------------------------------------------
    """)

    response = input().lower()

    while response != "x":


        # keep in a while loop
        response = input().lower()

if __name__ == "__main__":
    main()