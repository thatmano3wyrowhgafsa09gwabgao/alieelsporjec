Project Overview

This project is a simple Library Management System built with Python. It helps manage books, library members (patrons), and book loans. Users can be librarians, administrators, or patrons, each with different permissions for actions like adding books, registering members, or borrowing books.

Structure

The system includes:
- BookRecord: Represents a book with details like title, author, and quantity.
- PatronRecord: Represents a library member, including their name, ID, and role.
- TransactionRecord: Handles book loans, including the book's ISBN, patron's ID, and dates.
- LibraryManagement: Manages the library, including book and patron lists, and book loans.

Diagram: 

LibraryManagement System
|-> BookRecord
|-> PatronRecord
|-> TransactionRecord
|-> main() function
    |-> handle_staff_actions() helper function
    |-> get_book_details() helper function
    |-> get_patron_details() helper function



Usage Instructions

1. Setup: Place all `.py` files in one folder and run the main script using Python.
2. Login: Enter your user ID. If it's not recognized, you'll need to contact an administrator.
3. Using the System: Based on your role, you can add or remove books and patrons, borrow or return books, and administrators can change user roles.
4. Logging Out: Enter `0` to exit the system.

Findings, Challenges, and Improvements

- Handling Data: Managing real-time updates for books and patrons was a key challenge.
- Role Management: It was important to ensure that users could only do what their roles allowed.
- User Interface: Currently, it's text-based. A graphical interface could make it easier to use.
- Adding Features: Including overdue fines or a search feature could make the system more robust.
- Using a Database: For larger libraries, moving from JSON files to a database could improve performance.


1. Adding a Book

To add a book to the library, an administrator or librarian needs to follow these steps after logging into the system:

1. Select the option to "Register Book" from the menu.
2. When prompted, enter the details of the book, including title, author, ISBN, and quantity.
   - Example: `Enter book title: Harry Potter and the Sorcerer's Stone`
   - `Enter book author: J.K. Rowling`
   - `Enter book ISBN: 1234567890123`
   - `Enter quantity: 5`
3. Confirm the addition. The system should acknowledge that the book has been added.

2. Checking Out a Book

For a patron to check out a book, they (or a librarian on their behalf) would:

1. Log in to the system with their user ID.
2. Select the option to "Lend Book."
3. When prompted, enter the ISBN of the book they wish to borrow and their patron ID.
   - Example: `Enter book ISBN to lend: 1234567890123`
   - `Enter patron ID for book: patron001`
4. The system will process the request and confirm that the book has been checked out, along with the due date for return.

3. Generating Reports

To generate reports, such as a list of all books or all patrons, an administrator or librarian would:

1. Log in to the system with their user ID.
2. To generate a report of all books, select "List Books." The system will display a list of all books in the library, including their titles, authors, ISBNs, and available quantities.
3. To generate a report of all patrons, select "List Members." The system will display a list of all registered patrons, including their names, IDs, and contact information.




Conclusion

Creating this Library Management System offered insights into basic system design and user role management. While effective for simple library tasks, future updates could enhance usability and functionality.




code in actions screenshots : 
<img width="1470" alt="Screenshot 2024-03-07 at 12 21 37 AM" src="https://github.com/thatmano3wyrowhgafsa09gwabgao/alieelsporjec/assets/143622028/f3bb5486-c744-407c-9a41-9ea3dddc81bc">

<img width="1470" alt="Screenshot 2024-03-07 at 12 18 33 AM" src="https://github.com/thatmano3wyrowhgafsa09gwabgao/alieelsporjec/assets/143622028/93d67c3f-170c-4634-9447-ce879517fbe4">

