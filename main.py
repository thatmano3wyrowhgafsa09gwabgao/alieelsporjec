
from library_management import LibraryManagement
from book_record import BookRecord
from patron_record import PatronRecord

def main():
    library_system = LibraryManagement()
    print("Welcome to the Library System")

    user_id = input("Enter your ID to log in: ")
    user_profile = library_system.library_members.get(user_id, None)

    if not user_profile:
        print("User profile not found. Please contact the library admin.")
        return

    print(f"Logged in as: {user_profile['name']} ({user_profile['role']})")

    while True:
        print("\nMenu Options:")
        print("1. List Books")
        print("2. List Members")
        menu_options = ["1", "2"]

        if user_profile['role'] in ['librarian', 'administrator']:
            print("3. Register Book")
            print("4. Deregister Book")
            print("5. Register Patron")
            print("6. Deregister Patron")
            print("7. Lend Book")
            print("8. Collect Book")
            menu_options.extend(["3", "4", "5", "6", "7", "8"])

        if user_profile['role'] == 'administrator':
            print("9. Assign Role")
            menu_options.append("9")

        print("0. Logout")
        user_choice = input("Please make a selection: ").strip()

        if user_choice == "0":
            print("Thank you for using the Library System. Goodbye!")
            break

        if user_choice not in menu_options:
            print("Selection not recognized. Try again.")
            continue

        if user_choice == "1":
            library_system.display_books()
        elif user_choice == "2":
            library_system.display_patrons()
        elif user_choice in ["3", "4", "5", "6", "7", "8", "9"] and user_profile['role'] in ['librarian', 'administrator']:
            handle_staff_actions(user_choice, library_system, user_id, user_profile)
        else:
            print("Invalid option or insufficient permissions.")

def handle_staff_actions(choice, library, user_id, user_profile):
    if choice == "3":
        book_details = get_book_details()
        book_record = BookRecord(*book_details)
        library.register_book(book_record, user_id)
    elif choice == "4":
        isbn = input("Book ISBN to remove: ")
        library.deregister_book(isbn, user_id)
    elif choice == "5":
        patron_details = get_patron_details()
        patron_record = PatronRecord(*patron_details)
        library.register_patron(patron_record, user_id)
    elif choice == "6":
        patron_id = input("Patron ID to remove: ")
        library.deregister_patron(patron_id, user_id)
    elif choice == "7":
        isbn = input("Book ISBN to lend: ")
        patron_id = input("Patron ID for book: ")
        library.lend_book(isbn, patron_id, user_id)
    elif choice == "8":
        isbn = input("Book ISBN to collect: ")
        patron_id = input("Patron ID for return: ")
        library.collect_book(isbn, patron_id, user_id)
    elif choice == "9" and user_profile['role'] == 'administrator':
        patron_id = input("Patron ID for role update: ")
        new_role = input("New role (patron/librarian/administrator): ")
        library.assign_role(patron_id, new_role, user_id)

def get_book_details():
    title = input("Book title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    quantity = int(input("Quantity: "))
    return title, author, isbn, quantity

def get_patron_details():
    name = input("Patron name: ")
    patron_id = input("Patron ID: ")
    contact_info = input("Contact info: ")
    role = input("Role (patron/librarian/administrator): ")
    return name, patron_id, contact_info, role

if __name__ == "__main__":
    main()
