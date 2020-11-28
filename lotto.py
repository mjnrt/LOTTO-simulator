from random import randint

print('--- LOTTO simulator ---')
print('-- Pick 6 numbers in range of 1-49 --')

lotto_numbers = []
for _ in range(6):
    n = randint(1, 49)
    if n in lotto_numbers:
        n = randint(1, 49)
    lotto_numbers.append(n)

converting = True
while converting:
    try:
        player_numbers_str = input('Input your 6 numbers (separator is ",": ')
        player_numbers = player_numbers_str.split(',')
        int_list = []
        for i in player_numbers:
            if int(i) <= 49 and int(i) >= 1:
                i = int(i)
                int_list.append(i)
            else:
                raise ValueError('Not in range 1-49')
        converting = False
    except ValueError:
        print('Number not in range or letter. Try again..')

int_list = sorted(int_list)
print(f"Numbers you've picked: {int_list}")
print(f'Winning numbers: {lotto_numbers}')

win_numbers = []
for number in int_list:
    if number in lotto_numbers:
        win_numbers.append(number)

print(f'Numbers that match: {len(win_numbers)}')
