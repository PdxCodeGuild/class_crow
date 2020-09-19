import csv

def load():
    with open('/home/jpchato/class_crow/Code/jesse_pena/contacts.csv', 'r') as contacts:

        # reference: https://stackoverflow.com/a/50402818/14263621
        # reference: https://docs.python.org/2/library/csv.html
        reader = csv.DictReader(contacts)
        contacts_list = list(reader)

        print('These are the current contacts in your contact list')
        for contact in contacts_list:
            print('*' * 100)
            print(contact)
            print('*' * 100)
        
        while True:
            commands = input('create, read, update, delete, done? ')

            # create
            if commands == 'create':
                name = input('What is the name of the contact to add? ')
                favorite_fruit = input('What is their favorite fruit? ')
                favorite_color = input('What is their favorite color? ')
                contacts_list.append({
                    'name': name,
                    'favorite fruit': favorite_fruit,
                    'favorite color': favorite_color
                })
                with open('/home/jpchato/class_crow/Code/jesse_pena/contacts.csv', 'a', newline='') as contacts:
                    fieldnames = ['name', 'favorite fruit', 'favorite color']
                    writer = csv.DictWriter(contacts, fieldnames=fieldnames)
                    writer.writerow({'name': name, 'favorite fruit': favorite_fruit, 'favorite color': favorite_color})
                    print(contacts_list)

            # read
            if commands == 'read':
                for contact in contacts_list:
                    print(contact.get('name'))
                read_contact = input('What is the name of the contact whose information you need? ')
                
                for contact in contacts_list:
                    if contact['name'] == read_contact:
                        print(contact)

            # update
            if commands == 'update':
                for contact in contacts_list:
                    print(contact.get('name'))
                update_contact = input('What is the name of the contact whose information you need to update? ')
                update_attribute_category = input('Which attribute do you need to update? name, favorite fruit, favorite color? ')
                update_attribute_value = input('What is the new value ? ')
                for contact in contacts_list:
                    if contact['name'] == update_contact:
                        contact[update_attribute_category] = update_attribute_value
                        print(contact)
                    with open('/home/jpchato/class_crow/Code/jesse_pena/contacts.csv', 'w', newline='') as contacts:
                        fieldnames = ['name', 'favorite fruit', 'favorite color']
                        writer = csv.DictWriter(contacts, fieldnames=fieldnames)
                        writer.writeheader()
                        for contact in contacts_list:
                            writer.writerow(contact)
                        
            # delete
            # reference: https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/
            if commands == 'delete':
                for contact in contacts_list:
                    print(contact.get('name'))
                name_to_delete = input('What is the name of the contact to delete? ')
                for i in range(len(contacts_list)):
                    if contacts_list[i]['name'] == name_to_delete:
                        del contacts_list[i]
                with open('/home/jpchato/class_crow/Code/jesse_pena/contacts.csv', 'w', newline='') as contacts:
                        fieldnames = ['name', 'favorite fruit', 'favorite color']
                        writer = csv.DictWriter(contacts, fieldnames=fieldnames)
                        writer.writeheader()
                        for contact in contacts_list:
                            writer.writerow(contact)
                        
            if commands == 'done':
                print(contacts_list)   
                return False

        print(contacts_list)
        # return contacts_list
        
if __name__ == "__main__":
    load()
