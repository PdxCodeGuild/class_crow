def feet_to_meters():

    feet = input('How many feet do you need to convert to meters? ')
    meters = float(feet) * 0.3048

    print(f'The conversion is {meters} meters')

def units_to_meters():

    conversion_dict = {'feet': 0.3048, 'mile': 1609.34, 'kilometer': 1000, 'meter': 1, 'yard': 0.9144, 'inch': 0.0254}

    units = input('Which unit do you need to convert to meters? feet, mile, kilometer, meter, yard, or inch? ')

    length = input ('How many units do you need to convert? ')

    answer = conversion_dict.get(units)

    print('answer: ' + str(answer))

    print('length: ' + str(length))

    total = float(answer) * float(length)

    print('The conversion to meters is ' + str(total))

def users_choice():
    feet_to_any = {'feet': 1, 'mile': 0.000189394, 'kilometer': 0.0003048, 'meter': 0.3048, 'yard': 0.9144, 'inch': 12}

    miles_to_any = {'feet': 5280, 'mile': 1, 'kilometer': 1.60934, 'meter': 1609.34, 'yard': 1760, 'inch': 63360}

    km_to_any = {'feet': 3280.84, 'mile': 0.621371, 'kilometer': 1, 'meter': 1000, 'yard': 1093.61, 'inch': 39370.1}

    meters_to_any = {'feet': 0.3048, 'mile': 1609.34, 'kilometer': 1000, 'meter': 1, 'yard': 0.9144, 'inch': 0.0254}

    yards_to_any = {'feet': 3, 'mile': 0.000568182, 'kilometer': 0.0009144, 'meter': 0.91441, 'yard': 1, 'inch': 36}

    inches_to_any = {'feet': 0.0833333, 'mile': 0.0000157828, 'kilometer': 0.0000254, 'meter': 0.0254, 'yard': 0.0277778, 'inch': 1}

    starting_units = input('Which units are we converting from? feet, mile, kilometer, meter, yard, or inch?')

    ending_units = input('Which units are we converting to? feet, mile, kilometer, meter, yard, or inch? ')

    distance = int(input('What\'s the distance we\'re converting? '))

    if starting_units == 'feet':
        starting_conversion = feet_to_any.get(starting_units)
    elif starting_units == 'mile':
        starting_conversion = miles_to_any.get(starting_units)
    elif starting_units == 'kilometer':
        starting_conversion = km_to_any.get(starting_units)
    print(starting_conversion)


    

    
    # ending_conversion = conversion_dict.get(ending_units)

    # print(f'{starting_conversion} {ending_conversion}  {distance}')
    # answer = distance*starting_conversion*ending_conversion

    # print(answer)

if __name__ == "__main__":
    # feet_to_meters()
    # units_to_meters()
    users_choice()