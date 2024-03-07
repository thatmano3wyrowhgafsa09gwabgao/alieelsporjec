
class PatronRecord:
    # Initializing a new PatronRecord object with its essential details.
    def __init__(self, patron_name, patron_id, contact_details):
        # Assigning the parameters to instance variables for internal use.
        self.patron_name = patron_name
        self.patron_id = patron_id
        self.contact_details = contact_details

    # Method to display the patron's details in a structured format.
    def show_details(self):
        # Formatting the details into a readable string.
        details_format = "Name: {}, ID: {}, Contact: {}"
  
        print(details_format.format(self.patron_name, self.patron_id, self.contact_details))
