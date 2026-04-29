# Contact Book Application

contacts = []

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!\n")


# View Contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts available.\n")
        return

    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


# Search Contact
def search_contact():
    search_term = input("Enter name or phone to search: ").lower()

    found = False
    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone"]:
            print("\n🔍 Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True

    if not found:
        print("❌ Contact not found.\n")


# Update Contact
def update_contact():
    name = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Enter new details (leave blank to keep old value):")

            new_phone = input(f"New Phone ({contact['phone']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")

            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("✅ Contact updated successfully!\n")
            return

    print("❌ Contact not found.\n")


# Delete Contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!\n")
            return

    print("❌ Contact not found.\n")


# User Interface (Menu)
def menu():
    while True:
        print("====== 📱 Contact Book ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


# Run the program
menu()
