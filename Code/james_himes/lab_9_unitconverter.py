while True:
    print('welcome to the converter!')
    unit = input('What unit would you like to convert from? ft, mi, km, yd, in: ')
    distance = input('What is your distance?: ')
    distance = float(distance)
    conversion = {
        'ft': distance * 0.3048,
        'mi': distance * 1609.34,
        'km': distance * 1000,
        'yd': distance * 0.9144,
        'in': distance * 0.0254
    }
    print(f'Your new distance in meters is: {conversion[unit]}')
    repeat = input('would you like to convert something else? y/n ')
    if repeat == 'n':
        break
    elif repeat == 'y':
        continue
