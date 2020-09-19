import csv


def get_info(name,info):
    
    if info == '1':
        info = 'name'
    elif info == '2':
        info = 'address'
    elif info == '3':
        info = 'age'
    elif info == '4':
        info = 'favorite food'
    elif info == '5':
        with open('directory.csv', 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                if row.get('name') == name:
                    print('name:\t\t'+row.get('name'))
                    print('address:\t'+row.get('address'))
                    print('age:\t\t'+row.get('age'))
                    print('favorite food:\t'+row.get('favorite food'))
    if info != '5':
        with open('directory.csv', 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                if row.get('name') == name:
                    print(row.get(info))


def change_info(name,info,sub):
    if info == '1':
        info = 'name'
    elif info == '2':
        info = 'address'
    elif info == '3':
        info = 'age'
    elif info == '4':
        info = 'favorite food'
    elif info == '5':
        with open('directory.csv', 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                if row.get('name') == name:
                    csv_file[info] = sub
                    print('Success!: '+row)


def add_info(name, address, age, fav):
    with open('directory.csv', 'a', encoding='utf8') as file:
        file.write(name + ',' + address + ',' + age + ',' + fav)
    print('Success!: ' + name + ',' + address + ',' + age + ',' + fav)

def delete_info(name):
    new_list = []
    with open('directory.csv', 'r', encoding='utf8') as file:
        text = file.read()
        file_list = str(text).splitlines()
        final_list = []
        for item in file_list:
            final_list.append(item.split(','))
        for item in final_list:
            if item[0] != name:
                new_list.append(item)
    with open('directory.csv', 'w', encoding='utf8') as file:
        file.write('')
    with open('directory.csv', 'a', encoding='utf8') as file:
        for item in new_list:
            print(str(item))
            file.write(str(item).replace("[", '').replace(']', '').replace("'", '') + '\n')   

def main():

    while True:
        userinput = input('What would you like to do?\n1) Get info\n2)Change info\n3) Add info\n4)Delete\n: ')

        if userinput == '1':
            name = input('Enter a name to search: ')
            info = input('Select what info you want to get\n1) Name\n2) Address\n3) Age\n4) Favorite food\n5) All\n: ')
            get_info(name, info)
            
        if userinput == '2':
            name = input('Enter a name to search: ')
            info = input('Select what info you want to change\n1) Name\n2) Address\n3) Age\n4) Favorite food\n5) All\n: ')
            sub = input('Enter the desired data to substitute: ')
            change_info(name, info, sub)

        if userinput == '3':
            name = input('Enter a name: ')
            address = input('Enter an address: ')
            age = input('Enter an age: ')
            fav = input('Enter a favorite food: ')
            add_info(name, address, age, fav)

        if userinput == '4':
            name = input('Enter the name of the person you\'d like to delete: ')
            delete_info(name)

        loop = input('Would you like to search again? (Y/N): ').lower()

        if loop == 'n':
            break


main()


