from random import randint

lotto_numbers = []
for _ in range(6):
    n = randint(1, 49)
    if n in lotto_numbers:
        n = randint(1, 49)
    lotto_numbers.append(n)

converting = True
while converting:
    try:
        player_numbers_str = input('Input you 6 numbers (separator is ",": ')
        player_numbers = player_numbers_str.split(',')
        for i in range(6):
            player_numbers[i] = int(player_numbers[i])
        converting = False
    except ValueError:
        print('Number you picked is a letter or float. Try again..')

print(lotto_numbers)
print(player_numbers)
print(player_numbers in lotto_numbers)
