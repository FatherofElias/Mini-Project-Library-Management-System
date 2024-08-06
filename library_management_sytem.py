# This is the main course of the program; Library Management System

import re
from book import Book
from user import User
from author import Author

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

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
                print("Thank you for using the Library Management System!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user()
            elif choice == '3':
                self.display_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author()
            elif choice == '3':
                self.display_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    # Define methods for book operations
    def add_book(self):
        try:
            title = input("Enter book title: ")
            author_name = input("Enter book author: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")

            # Validate publication date format
            if not re.match(r"\d{4}-\d{2}-\d{2}", publication_date):
                raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

            # Check if the author already exists
            author = next((author for author in self.authors if author.get_name() == author_name), None)
            if not author:
                biography = input("Enter author biography: ")
                author = Author(author_name, biography)
                self.authors.append(author)
                print(f"Author '{author_name}' added successfully.")

            new_book = Book(title, author_name, genre, publication_date)
            self.books.append(new_book)
            print(f"Book '{title}' by {author_name} added successfully.")
        except ValueError as e:
            print(e)



    def borrow_book(self):
        try:
            library_id = input("Enter your library ID: ")
            user = next((user for user in self.users if user.get_library_id() == library_id), None)
            if not user:
                print(f"User with Library ID '{library_id}' not found.")
                return

            title = input("Enter book title to borrow: ")
            for book in self.books:
                if book.get_title() == title and book.is_available():
                    book.borrow()
                    user.borrow_book(title)
                    print(f"Book '{title}' borrowed successfully.")
                    return
            print(f"Book '{title}' not found or already borrowed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def return_book(self):
        try:
            library_id = input("Enter your library ID: ")
            user = next((user for user in self.users if user.get_library_id() == library_id), None)
            if not user:
                print(f"User with Library ID '{library_id}' not found.")
                return

            title = input("Enter book title to return: ")
            for book in self.books:
                if book.get_title() == title and not book.is_available():
                    book.return_book()
                    user.return_book(title)
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