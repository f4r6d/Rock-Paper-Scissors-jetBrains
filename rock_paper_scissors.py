import random

name = input('Enter your name: ')
print(f'Hello, {name}')

def check_score(name):
    rating = open('rating.txt', 'r')
    rating_list = rating.readlines()
    for row in rating_list:
        if name in row:
            return int(row[row.find(' ') + 1 :]) 
            break
        else:
            return 0
    rating.close()

first_check = check_score(name)

if first_check == 0:
    rating = open('rating.txt', 'a')
    new_row = name + ' 0\n'
    rating.write(new_row)
    rating.close()

options = input()
if options:
    shapes = options.split(',')
else:
    shapes = ['rock', 'paper', 'scissors']

print("Okay, let's start")

winning = []
for i in range(1, len(shapes)):
    if i <= len(shapes) / 2:
        winning.append(i)
    else:
        winning.append(-i)
        
def update_file(name, new_score):
    rating = open('rating.txt', 'r')
    rating_list = rating.readlines()
    for row in rating_list:
        if name in row:
            row_index = rating_list.index(row)        
    rating.close()
    rating_list[row_index] = name + ' ' + str(new_score) + '\n'   
    updated_rating = open('rating.txt', 'w')
    updated_rating.writelines(rating_list)
    rating.close()
    
def state(player, com):
    if shapes.index(player) == shapes.index(com):
        return 'draw'
    elif shapes.index(player) - shapes.index(com) in winning:
        return 'win'
    else:
        return 'lose'

def result(player, com):        
    if state(player, com) == 'lose':
        print(f'Sorry, but the computer chose {com}')
    elif state(player, com) == 'draw':
        new_score = check_score(name) + 50
        update_file(name, new_score)
        print(f'There is a draw ({com})')
    elif state(player, com) == 'win':
        new_score = check_score(name) + 100
        update_file(name, new_score)
        print(f'Well done. The computer chose {com} and failed')

game = 'on'
while game:
    player = input()
    if player == '!exit':
        game = ''
    elif player == '!rating':
        print(f'Your rating: {check_score(name)}')
    elif player in shapes:
        com = random.choice(shapes)
        result(player, com)
    else:
        print('Invalid input') 