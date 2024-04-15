def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    contacts[name.lower()] = {'phone': phone, 'email': email}
    print(f"Contact added/updated for {name.title()}.")

def view_contacts(contacts):
    if contacts:
        for name, info in contacts.items():
            print(f"\nName: {name.title()}\nPhone: {info['phone']}\nEmail: {info['email']}")
    else:
        print("No contacts available.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if contacts.pop(name.lower(), None):
        print(f"Contact for {name.title()} deleted successfully.")
    else:
        print(f"No contact found for {name.title()}.")