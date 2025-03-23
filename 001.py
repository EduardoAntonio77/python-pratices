while True:
    # verifying if the number is even or odd
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('Please enter a valid integer.')
        continue

    if (number % 2) == 0:
        print(f'The number {number} is even!')
    else:
        print(f'The number {number} is odd!')
    
    # asking the user if they want to continue
    while True:
        userResponse = input('Do you want to continue entering numbers? (y/n): ').strip().lower()
        if userResponse == 'y':
            break
        elif userResponse == 'n':
            print("Exiting the program.")
            break
        else:
            print('Enter a valid response! (y/n)')

    if userResponse == 'n':
        break