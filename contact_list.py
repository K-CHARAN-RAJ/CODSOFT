contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact added successfully.")

    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}")

    elif choice == '3':
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            info = contacts[search_name]
            print(f"Name: {search_name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
        else:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter name of contact to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == '5':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
