from random import randint

count = 0
random_number = randint(1, 100)
while count < 10:
    guess = int(input('Please, try to guess the number from 1 to 100: '))
    count += 1
    print(random_number)
    if random_number == guess:
        print('WIN!!!')
        break
    if random_number > guess:
        print('Try higher number')
    if random_number < guess:
        print('Try lower number')
else:
    print('It was the last chance, please try again')
