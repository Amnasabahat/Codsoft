import os
import json

# Initialize an empty list to store contacts
contacts = []

# Function to load contacts from a JSON file
def load_contacts():
    global contacts
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
# Function to save contacts to a JSON file
def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")

    if name and phone and email and address:
        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        contacts.append(contact)
        save_contacts()
        print(f"{name} added to contacts.")
    else:
        print("Name, phone, email, and address are required fields.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    found = False
    for contact in contacts:
        if contact["Name"] == name:
            contacts.remove(contact)
            found = True
            save_contacts()
            print(f"{name} deleted from contacts.")
            break
    if not found:
        print(f"{name} not found in contacts.")

# Function to search for a contact
def search_contact():
    search_term = input("Enter a name to search for: ")
    search_results = []

    for contact in contacts:
        if search_term.lower() in contact["Name"].lower():
            search_results.append(contact)

    if search_results:
        print("\nSearch results:")
        for result in search_results:
            print(f"Name: {result['Name']} | Phone: {result['Phone']} | Email: {result['Email']} | Address: {result['Address']}")
    else:
        print("No matching contacts found.")

# Function to edit a contact
def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    found = False
    for contact in contacts:
        if contact["Name"] == name:
            print("\nCurrent information:")
            print(f"Name: {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']} | Address: {contact['Address']}")
            new_phone = input("Enter new phone (leave empty to keep current): ")
            new_email = input("Enter new email (leave empty to keep current): ")
            new_address = input("Enter new address (leave empty to keep current): ")

            if new_phone:
                contact['Phone'] = new_phone
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address

            save_contacts()
            print(f"{name}'s information updated.")
            found = True
            break
    if not found:
        print(f"{name} not found in contacts.")

# Function to display all contacts
def display_contacts():
    print("\nAll Contacts:")
    for contact in contacts:
        print(f"Name: {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']} | Address: {contact['Address']}")

# Load contacts from a file when the program starts
load_contacts()

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        edit_contact()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Contact Book!")
