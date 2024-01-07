# contact book

# contact information
contacts = []


def add_contact(name, phone, email, address):
    contact = {'Name': name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print(f"{contact['Name']} contact was sucessfully added")


# view contact

def view_contact_list():
    if not contacts:
        print("contact book is empty")
    else:
        for person in contacts:
            print(f"Name : {person['Name']}  Phone : {person['Phone']}")


# search contact

def search_contact(search_contact_input):
    for name in contacts:
        if name['Name'].lower() == search_contact_input or str(name['Phone']) == search_contact_input:
            print(f" Name :{name['Name']} , Phone : {name['Phone']} , Email : {name['Email']} , Address : {name['Address']}")
        else:
            print(f"{search_contact_input} is not there in contact list ")


def update_contact(update_name):
    for name in contacts:
        if name['Name'] == update_name:
            print("enter name to update user name")
            print("enter phone to update phone number")
            print("enter email to update user email ")
            print("enter address to update user address")
            user_choice = input("enter your operation : ")
            if user_choice == 'name':
                enter_name = input("enter name to update : ").lower()
                name['Name'] = enter_name
            elif user_choice == 'phone':
                enter_name = input("enter phone to update : ").lower()
                name['Phone'] = enter_name
            elif user_choice == 'email':
                enter_name = input("enter email to update : ").lower()
                name['Email'] = enter_name
            elif user_choice == 'address':
                enter_name = input("enter address to update : ").lower()
                name['address'] = enter_name
            else:
                print(f"{update_name} is not there in contact list  ")


# Delete contact

def contact_delete(name_to_delete):
    for name in contacts:
        if name['Name'] == name_to_delete:
            contacts.remove(name)
            print(f"contact {name_to_delete} deleted sucessfully ")
        else:
            print(f"{name_to_delete} is not there in contact list  ")


# main body of program

open = True
while open:
    print("enter 1 to add contact ")
    print("enter 2 to view contacts ")
    print("enter 3 to search contact ")
    print("enter 4 to update contact ")
    print("enter 5 to delete contact ")
    your_option = input("enter your option : ")
    if your_option == '1':
        name = input("enter the name : ")
        phone = input("enter phone number : ")
        email = input("enter email : ")
        address = input("enter address : ")
        add_contact(name,phone,email,address)
    elif your_option == '2':
        view_contact_list()
    elif your_option == '3':
        print("please enter name or phone number to search contact")
        search_contact_input = input("enter name or phone number to search for contact ").lower()
        search_contact(search_contact_input)
    elif your_option == '4':
        update_name = input("enter name of the contact to update : ").lower()
        update_contact(update_name)
    elif your_option == '5':
        name_to_delete = input("enter name to delete contact    : ")
        contact_delete(name_to_delete)





