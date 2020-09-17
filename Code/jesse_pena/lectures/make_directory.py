import csv

with open('directory.csv', mode='w') as directory:
    fieldnames = ['name', 'address', 'age', 'height', 'favorite food']
    writer = csv.DictWriter(directory, fieldnames=fieldnames)

    writer.writeheader()
    
    writer.writerow({'name': 'CJ', 'address': '16 1st st', 'age': '1', 'height': '2ft', 'favorite food':'kibble'})
    writer.writerow({'name': 'john smith', 'address': '123 street', 'age': '42', 'height': '5ft', 'favorite food':'cheese'})
    writer.writerow({'name': 'guy man', 'address': '69 house street', 'age': '24', 'height': '6ft', 'favorite food': 'bread'})

def find_contact(contacts_list, contact_lookup):
    for i, contact in enumerate(contacts_list):
        if contact['name'] == contact_lookup:
            return i
    return -1

def create(contacts_list, contact):
    contacts_list.append(contacts_list)
    return contacts_list[-1]


def main():
    data = '/home/jpchato/class_crow/Code/jesse_pena/labs/contacts.csv'
    valid_inputs =['h', 'help', 'commands', 
                    'c', 'create',
                    'r', 'read',
                    'u', 'update',
                    'd', 'delete',
                    'l', 'list',
                    'load',
                    'save',
                    'x', 'exit'
    ]
    while True:
        while True:
            command = input('What operation would you like to perform? ').strip().lower()
            if command in valid_inputs:
                break
            list_commands()

            # create save function

        if command.startswith('c') or command.startswith('u'):
            contact = {}
            for atrribute_name in header:
                atrribute_value = input(f'what is the contact\'s name {attribute_name}?')
                contact[atrribute_name] = atrribute_value
            if command.startswith('c'):
                create(contacts_list, contact)
            else:
                cereal = {k:v for {k:v} in cereal.items() in v}
                update(cereals, cereal['name'], cereal)
        elif command.startswith('r'):
            contact_name = input('What is the name of the contact you would like to retrieve? ')
            contact - read(contacts_list, contact_name)
        


        

# delete with .pop(index)
# save with 