import random
number=random.randint(0,100)
is_num=True

prompt=input('I\'m thinking of a number beteen 0 and 100. What number am I thinking of? : ')
try:
    prompt=int(prompt)
except ValueError:
    is_num=False

def game():
    if is_num:
        if prompt>100:
            print('That number is too big')
        elif prompt>number:
            comparison=prompt-number
            print('I was thinking of '+str(number)+' Your number is greater than mine by '+str(comparison))
        elif prompt<number:
            comparison=number-prompt
            print('I was thinking of '+str(number)+' Your number is lesser than mine by '+str(comparison))
        else:
            print('that\'s the number I was thinking of.')
    elif not is_num:
        print('not a number')
while not is_num:
    prompt=input('try again: ')
    is_num=True
game() 