beanie_babies = [{'name':'Brown Bear', 'size':'large', 'Animal Type':'Bear'},
                { 'name': 'Shortie', 'size': 'small', 'Animal Type': 'Mosquito'},
                {'name':'Speedy', 'size': 'medium', 'Animal Type': 'Turtle'}
                ]
                
# create
def create(dict_list):
    dict_list.append({'name': 'Steve', 'size': 'large', 'Animal Type': 'Whale'})
    print(dict_list)

# read
def read(dict_list):
    for dictionary in dict_list: 
        print(dictionary)
# update
def update(dict_list, attribute):
    for dictionary in dict_list:
        if dictionary[attribute] == 'Brown Bear':
            dictionary[attribute] = 'UPDATED'
    print(dict_list)

# delete
def delete(dict_list):
    for dictionary in dict_list:
        if dictionary['name'] == 'UPDATED':
            dict_list.remove(dictionary)
    print(dict_list)

create(beanie_babies)
update(beanie_babies, 'name')
read(beanie_babies)
delete(beanie_babies)