dist = int(input('Enter your distance for conversion: '))
unit1 = input('Enter your initial units of measure (ft, mi, m, km): ')
unit2 = input('Enter your desired conversion (ft, mi, m, km): ')

if unit1 == 'ft':
    meters = dist * 0.3048
elif unit1 == 'mi':
    meters = dist * 1609.34
elif unit1 == 'm':
    meters = dist
elif unit1 == 'km':
    meters = 1000

print(meters)

if unit2 == 'ft':
    conversion = float(meters / 0.3048)
elif unit2 == 'mi':
    conversion = float(meters / 1609.34)
elif unit2 == 'm':
    conversion = float(meters)
elif unit2 == 'km':
    conversion = float(meters / 1000)


print(f'{dist} {unit1} is {conversion:.4f} {unit2}!')
