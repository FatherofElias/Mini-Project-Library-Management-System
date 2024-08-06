# This is the main course of the program; Library Management System


import re
import os
from book import Book
from user import User
from author import Author

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.load_data()

    def load_data(self):
        self.load_books()
        self.load_users()
        self.load_authors()

    def save_data(self):
        self.save_books()
        self.save_users()
        self.save_authors()

    def load_books(self):
        if os.path.exists('books.txt'):
            with open('books.txt', 'r') as file:
                for line in file:
                    title, author, genre, publication_date, is_available = line.strip().split(',')
                    book = Book(title, author, genre, publication_date)
                    if is_available == 'False':
                        book.borrow()
                    self.books.append(book)

    def save_books(self):
        with open('books.txt', 'w') as file:
            for book in self.books:
                file.write(f"{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_publication_date()},{book.is_available()}\n")

    def load_users(self):
        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as file:
                for line in file:
                    name, library_id, borrowed_books = line.strip().split(',')
                    user = User(name, library_id)
                    user.borrow_book(borrowed_books.split(';'))
                    self.users.append(user)

    def save_users(self):
        with open('users.txt', 'w') as file:
            for user in self.users:
                borrowed_books = ';'.join(user.get_borrowed_books())
                file.write(f"{user.get_name()},{user.get_library_id()},{borrowed_books}\n")

    def load_authors(self):
        if os.path.exists('authors.txt'):
            with open('authors.txt', 'r') as file:
                for line in file:
                    name, biography = line.strip().split(',')
                    author = Author(name, biography)
                    self.authors.append(author)

    def save_authors(self):
        with open('authors.txt', 'w') as file:
            for author in self.authors:
                file.write(f"{author.get_name()},{author.get_biography()}\n")

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.save_data()
                print("Thank you for using the Library Management System!")
                break
            else:
                print("Invalid choice. Please try again.")

    # Define methods for book operations
    def add_book(self):
        try:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")

            # Validate publication date format
            if not re.match(r"\d{4}-\d{2}-\d{2}", publication_date):
                raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

            new_book = Book(title, author, genre, publication_date)
            self.books.append(new_book)
            print(f"Book '{title}' by {author} added successfully.")
        except ValueError as e:
            print(e)

    def borrow_book(self):
        try:
            title = input("Enter book title to borrow: ")
            for book in self.books:
                if book.get_title() == title and book.is_available():
                    book.borrow()
                    print(f"Book '{title}' borrowed successfully.")
                    return
            print(f"Book '{title}' not found or not available.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def return_book(self):
        try:
            title = input("Enter book title to return: ")
            for book in self.books:
                if book.get_title() == title and not book.is_available():
                    book.return_book()
                    print(f"Book '{title}' returned successfully.")
                    return
            print(f"Book '{title}' not found or already available.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search_book(self):
        try:
            title = input("Enter book title to search: ")
            for book in self.books:
                if book.get_title() == title:
                    print(f"Book found: '{title}' by {book.get_author()}, Genre: {book.get_genre()}, Published on: {book.get_publication_date()}, Available: {book.is_available()}")
                    return
            print(f"Book '{title}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_books(self):
        try:
            if not self.books:
                print("No books available.")
            else:
                print("Books available:")
                for book in self.books:
                    print(f"'{book.get_title()}' by {book.get_author()}")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Define methods for user operations
    def add_user(self):
        try:
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")

            # Validate library ID format (e.g., must be alphanumeric)
            if not re.match(r"^[a-zA-Z0-9]+$", library_id):
                raise ValueError("Invalid library ID format. Please use alphanumeric characters.")

            new_user = User(name, library_id)
            self.users.append(new_user)
            print(f"User '{name}' added successfully.")
        except ValueError as e:
            print(e)

    def view_user(self):
        try:
            library_id = input("Enter library ID to view details: ")
            for user in self.users:
                if user.get_library_id() == library_id:
                    print(f"User found: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {user.get_borrowed_books()}")
                    return
            print(f"User with Library ID '{library_id}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_users(self):
        try:
            if not self.users:
                print("No users available.")
            else:
                print("Users available:")
                for user in self.users:
                    print(f"User: {user.get_name()}, Library ID: {user.get_library_id()}")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Define methods for author operations
    def add_author(self):
        try:
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            new_author = Author(name, biography)
            self.authors.append(new_author)
            print(f"Author '{name}' added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_author(self):
        try:
            name = input("Enter author name to view details: ")
            for author in self.authors:
                if author.get_name() == name:
                    print(f"Author found: {author.get_name()}, Biography: {author.get_biography()}")
                    return
            print(f"Author '{name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_authors(self):
        try:
            if not self.authors:
                print("No authors available.")
            else:
                print("Authors available:")
                for author in self.authors:
                    print(f"Author: {author.get_name()}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Create an instance of the LibraryManagementSystem and run the main menu
if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.main_menu()