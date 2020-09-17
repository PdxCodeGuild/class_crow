import csv 

with open('directory.csv', mode='w') as directory: 
    fieldnames= ['name', 'address', 'age', 'favorite food']
    writer =  csv.DictWriter(directory, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'CJ', 'address':'16 1st St', 'age': '1', 'favorite food':'kibble'})
    writer.writerow({'name': 'John Smith', 'address':'123 Lake Lane', 'age':'62', 'favorite food':'Pasta'})
    writer.writerow({'name': 'Erica Jones', 'address':'87 Sixth St', 'age':'26', 'favorite food':'Mangoes'})