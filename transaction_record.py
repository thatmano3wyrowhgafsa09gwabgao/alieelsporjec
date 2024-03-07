from datetime import datetime, timedelta


class TransactionRecord:
    # Initializing a TransactionRecord with book and patron identifiers, and optional dates.
    def __init__(self, book_isbn, patron_id, checkout_date=None, due_date=None, is_returned=False):
        self.book_isbn = book_isbn
        self.patron_id = patron_id
        # Set the checkout date to now if not specified.
        self.checkout_date = checkout_date if checkout_date else datetime.now()
        # Set the due date to two weeks from checkout date if not specified.
        self.due_date = due_date if due_date else self.checkout_date + timedelta(days=14)
        self.is_returned = is_returned

    # Method to update the transaction status to indicate the item has been returned.
    def set_as_returned(self):
        self.is_returned = True
