# user_age = 'a27'
# user_age.isdigit()

# user_name = 'Alex'
# print(user_name)
# print(user_name.strip())
# print(user_name.lower())

users = ['Alex', 'Bob']
user_age = input('Ведите ваш возраст ')
user_name = input('Введите ваш логин: ')

while True:
    if user_name == users:
        if user_age.isdigit():
            user_age = int(user_age)
            if user_age > 100:
                print ('Некорректное значение')
            else:
                print('Данные записаны')
        else:
            print('Вы ввели некорректный тип данных')
    else:
        print('Такого пользователя не существует!')
        print('Хотите пройти регистрацию?')
        user_cmd = input('1. Да\n 2. Нет\n')
        if user_cmd == '1':
            user_age = input('Ведите ваш возраст ')
            user_name = input('Введите ваш логин: ')

        user_cmd = input('Хотите продолжить? \n Да \n Нет \n')
        if user_cmd == '2':
            break









