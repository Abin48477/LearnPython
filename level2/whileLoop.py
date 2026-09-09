secrete_num = 4
guess = 0
while guess != secrete_num:
    guess =int(input('Guess the number(1-10):'))
    if guess != secrete_num:
        print('Wrong! Try again.')

print('You got it!')
