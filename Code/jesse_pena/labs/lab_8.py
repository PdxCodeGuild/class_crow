def make_change():

    pennies = input('How many pennies are there? ')
    pennies = int(pennies)

    quarters = pennies // 25

    

    pennies = pennies - quarters*25

    dimes = pennies // 10

    pennies = pennies - dimes*10

    nickels = pennies // 5

    pennies = pennies - nickels*5

    print(f'There are {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.')

def make_dollar():
    dollars = input('How many dollars are there? (i.e. 1.25, .75, 2.22) ')
    dollars = float(dollars)
    pennies = dollars / 0.01
    print(f'There are {pennies} pennies')

if __name__ == "__main__":
    make_change()
    make_dollar()