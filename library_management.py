
import json

from book_record import BookRecord
from patron_record import PatronRecord
from transaction_record import TransactionRecord

class LibraryManagement:
    def __init__(self):
        # Load initial data
        self.book_catalog = self._load_books()
        self.library_members = self._load_patrons()
        self.book_loans = []

    def _load_books(self):
        # Load book data from a JSON file
        try:
            with open('books_catalog.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_books(self):
        # Save the current state of books to a JSON file
        with open('books_catalog.json', 'w') as file:
            json.dump(self.book_catalog, file, indent=4)

    def _load_patrons(self):
        # Load patron data from a JSON file
        try:
            with open('library_members.json', 'r') as file:
                members = json.load(file)
        except FileNotFoundError:
            members = {}

        admin_id = "admin-001"
        if admin_id not in members:
            print(f"Creating default admin account with ID: {admin_id}")
            members[admin_id] = {
                "name": "Library Admin",
                "patron_id": admin_id,
                "contact_info": "admin@library.com",
                "role": "administrator"
            }
            self._save_patrons(members)
        return members

    def _save_patrons(self, patrons=None):
        if patrons is None:
            patrons = self.library_members
        with open('library_members.json', 'w') as file:
            json.dump(patrons, file, indent=4)

    def register_book(self, book_record, user_id):
        # Allows a user with appropriate permissions to add a book to the catalog
        user = self.library_members.get(user_id)
        if user and user['role'] in ['librarian', 'administrator']:
            if book_record.book_isbn in self.book_catalog:
                print("Book exists. Updating quantity.")
                self.book_catalog[book_record.isbn]['quantity'] += book_record.quantity
            else:
                self.book_catalog[book_record.isbn] = vars(book_record)
            self._save_books()
        else:
            print("Permission denied for adding books.")

    def deregister_book(self, isbn, user_id):
        # Allows a user with appropriate permissions to remove a book from the catalog
        user = self.library_members.get(user_id)
        if user and user['role'] in ['librarian', 'administrator']:
            if isbn in self.book_catalog:
                del self.book_catalog[isbn]
                self._save_books()
                print(f"Book {isbn} removed.")
            else:
                print("Book not found.")
        else:
            print("Permission denied for removing books.")


    # Example method signature after refactoring for adding a patron
    def register_patron(self, patron_record, user_id):
        user = self.library_members.get(user_id)
        if user and user['role'] == 'administrator':
            self.library_members[patron_record.patron_id] = vars(patron_record)
            self._save_patrons()
        else:
            print("Permission denied for adding patrons.")
