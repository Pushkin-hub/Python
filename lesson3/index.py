# users_dict = {'name', 'Alex'}
# users_dict['name'] = 'Bob'


# users_dict = {
#     'id': {
#         'name': 'Alex',
#         'age': 26,
#         'phoneNumber': '+79998887766'
#     },
#     'id2': {
#         'name': 'Bob',
#         'age': 25,
#         'phoneNumber': '+79778877888'
#     },
#     'id3': {
#         'name': 'Ann',
#         'age': 18,
#         'phoneNumber': '+79821112233'
#     }
# }
# print(users_dict['id']['name'])

# users_dict.update({'id2':{
#     'name': 'Bob',
#     'age': 27,
#     'phoneNumber': '+79885554433'
# }})

# users_dict.pop('id', 'Такого пользователя не существует')


import random
deck = []

dealer = {
    'hard':[],
    'score': 0
}
player = {
    'hard':[],
    'score': 0
}

for name in range(2, 15):
    for suit in ['Крести', 'Пики', 'Буби', 'Черви']:
        card = {
            'name': name,
            'suit': suit,
            'cost': name
        }

        if name > 10:
            card['suit'] = suit
            if name == 11:
                card['name'] = 'J'
                card['cost'] = 2
            elif name == 12:
                card['name'] = 'Q'
                card['cost'] = 3
            elif name == 13:
                card['name'] = 'K'
                card['cost'] = 4
            elif name == 14:
                card['name'] = 'A'
                card['cost'] = 11

        deck.append(card)

random.shuffle(deck)

for _ in range(2):
    card = deck.pop()
    player['hard'].append(card)
    card = deck.pop()
    dealer['hard'].append(card)

for hand in player["hard"]:
    print(f'Ваши карты: {hand['name']} {hand['suit']}')

while True:

    while True:
        question = input('Желаете ли вы взять карту? (yes/no)')
        if question == 'yes':
            card = deck.pop()
            player['hard'].append()
            player['score'] += card['cost']
        elif question == 'no':
            break

    if player['score'] == dealer['score']:
        print('Ничья!')
    elif player['score'] > dealer['score']:
        print('Выиграл!')
    elif player['score'] < dealer['score']:
        print('Проиграл!')