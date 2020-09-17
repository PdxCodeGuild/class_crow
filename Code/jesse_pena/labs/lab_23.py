import csv

# [
#   {'name': 'Jesse Pena', ' favorite fruit': ' mango', ' favorite color': ' blue'}, 
#   {'name': 'Jessica Andrade', ' favorite fruit': ' strawberries', ' favorite color': ' purple'}
# ]

def load():
    with open('/home/jpchato/class_crow/Code/jesse_pena/labs/contacts.csv', 'r') as contacts:

        # reference: https://stackoverflow.com/a/50402818/14263621
        # reference: https://docs.python.org/2/library/csv.html
        reader = csv.DictReader(contacts)
        contacts_list = list(reader)

        commands = input('create, read, update, delete? ')

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

        # read
        if commands == 'read':
            read_contact = input('What is the name of the contact whose information you need? ')
            for contact in contacts_list:
                if contact['name'] == read_contact:
                    print(contact)

        # update
        if commands == 'update':
            update_contact = input('What is the name of the contact whose information you need to update? ')
            update_attribute_category = input('Which attribute do you need to update? name, favorite fruit, favorite color? ')
            update_attribute_value = input('What is the new value ? ')
            for contact in contacts_list:
                if contact['name'] == update_contact:
                    contact[update_attribute_category] = update_attribute_value
                    print(contact)

        # delete
        if commands == 'delete':
            name_to_delete = input('What is the name of the contact to delete? ')
            for contact in contacts_list:
                if contact['name'] == name_to_delete:
                    contact.clear()
                print(contacts_list)





        # print(contacts_list)
        # return contacts_list




if __name__ == "__main__":
    load()
