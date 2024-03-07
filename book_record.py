# Importing the json module for potential future JSON operations.
import json

# Define the Book class to encapsulate book details.
class BookRecord:
    def __init__(self, book_title, book_author, book_isbn, available_quantity):
        self.book_title = book_title
        self.book_author = book_author
        self.book_isbn = book_isbn
        self.available_quantity = available_quantity


    # Method to print the book's details in a formatted manner.
    def show_details(self):
        # Creating a formatted string with book details.
        detail_string = "Title: {}, Author: {}, ISBN: {}, Available Quantity: {}"
        # Printing the formatted string with book information.
        print(detail_string.format(self.book_title, self.book_author, self.book_isbn, self.available_quantity))

