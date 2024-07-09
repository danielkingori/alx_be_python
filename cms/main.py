from module import *
def main():
    while True:
        print("1. Add a contact")
        print("2. View a contact")
        print("3. Search a contact")
        print("4. Update a contac")
        print("5. Delete a contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            contact_name = input("Enter name: ")
            number = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contact_name, number, email)
            
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            name_to_search = input("Enter a name:")
            search_contact(contacts, name_to_search)
        elif choice == "4":
            name_to_update = input("Enter a name: ")
            new_num =  input("Enter new number:")
            new_email = input("Enter a new email: ")
            update_contact(name_to_update,
                            new_num if new_num else None,
                            new_email if new_email else None)
        elif choice == "5":
            name_to_delete =  input("Enter a name:")
            delete_contact(contacts, name_to_delete)
        elif choice == "6":
            print("Exiting")
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()