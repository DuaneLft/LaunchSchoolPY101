
def yes_no_response(question):
    while True:
        print(question)
        answer = input()

        if answer == 'y' or answer == 'yes':
            print('Here we go again!')
            return
        elif answer == 'n' or answer == 'no':
            print('Okay. See you later.')
            return
        else:
            print('You goofed! That is not a valid answer.')