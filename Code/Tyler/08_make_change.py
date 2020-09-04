amount = int(input('HOW MANY PENNIES YOU GOT!? '))
out = float(amount / 100)

print(f'Ight, that\'s ${out:.2f}.\n')

wish = input('How much money would you like to have? ')

if '$' in wish:
    wish = wish.replace('$', '')
wish = float(wish)
pennies = int(wish * 100)

print(f'Dang, that\'s {pennies} pennies!')