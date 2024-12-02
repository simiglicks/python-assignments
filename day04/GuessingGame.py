from random import randint


def guess_the_number(number):
    user_guess = None
    num_guess = 0
    while user_guess != number:
        user_guess = input('Guess a number: ')
        if user_guess == 'x':
            return False  # just exit
        if user_guess == 'n':
            return True # ask to play again
        if user_guess == 's':
            print(number)
        elif user_guess.isnumeric():  # check for number
            int_user_guess = int(user_guess)
            num_guess += 1
            if int_user_guess > number:
                print('Too big')
            elif int_user_guess < number:
                print('too small')
            else:
                print('you win!')
                print('number of guesses:', num_guess)
                return True

def main():
    START = 1
    STOP = 20
    play_game = True
    while play_game:
        # generate random number
        number = randint(START, STOP)
        result = guess_the_number(number)
        if not result:
            return  # the user pressed 'x'
        play_prompt = ''
        while play_prompt.lower() not in ['yes', 'no']:
            play_prompt = input('Do you want to play again (yes/no)? ')
        if play_prompt.lower() == 'no':
            play_game = False
main()