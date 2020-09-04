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
    conversion_dict = {'feet': 0.3048, 'mile': 1609.34, 'kilometer': 1000, 'meter': 1, 'yard': 0.9144, 'inch': 0.0254}
    units_from = input('Which unit do you need to convert from? feet, mile, kilometer, meter, yard, or inch? ')
    units_to = input('Which unit do you need to convert to? feet, mile, kilometer, meter, yard, or inch? ')
    length = input ('What\'s the distance to convert? ')

    conversion_to_meters = conversion_dict.get(units_from)
    print(conversion_to_meters)
    print(length)
    distance_in_meters = float(length) * float(conversion_to_meters)
    print(distance_in_meters)
    answer =  distance_in_meters / conversion_dict.get(units_to)
    print(f'Distance of {length} {units_from} to {units_to} is {answer}')


if __name__ == "__main__":
    feet_to_meters()
    units_to_meters()
    users_choice()