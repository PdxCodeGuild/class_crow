
def main():
    nums = []
    counter = 0
    while True:
        userinput = input('\nEnter a number or "done" when finished: ').lower()
        if userinput != "done":
            nums.append(int(userinput))
            counter += 1
        else:
            break

    total = 0
    for item in nums:
        total = total + item

    average = total / counter

    print(f'Average: {average}')

main()