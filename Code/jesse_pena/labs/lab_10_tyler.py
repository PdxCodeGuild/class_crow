def main():
    nums = []
    counter = 0
    while True:
        user_input = input('\nEnter a number or "done" when finished: ').lower()
        if user_input != "done":
            nums.append(int(user_input))
            counter += 1
        else:
            break

    total = 0
    for item in nums:
        total = total + item

    average = total / counter

    print(f'Average: {average}')

if __name__ == "__main__":
    main()