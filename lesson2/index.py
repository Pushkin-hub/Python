# age = 60

# if  age > 30:
#     print('комната 1')
# elif age >= 18:
#     print('комната 2')
# else:
#     print('В доступе отказано!')



# while True:
#     number = input('Введите число: ')
#     if number.isdigit():
#         number = int(number)
#         print('Строка преобразована в число')
#         break
#     else:
#         print('Неверный формат')
        
# if number % 2 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 2 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print('Bad')
    


# names = 'Alex Bob Sam'
# names += 'Nick'

# print(names)
# # names[0] = 'a'
# list_names = ['Alex', 'Bob', 'Sam', 'Sam', 'Sam']
# print(list_names)
# list_names[0] = 'Anna'
# print(list_names)

# list_names += ['Nick']
# list_names.append('Max')

# list_names.pop(0)
# required_name = input('Введите имя которое хотите удалить: ')
# for name in list_names:
#     if name == required_name:
#         list_names.remove(name)

# print(list_names)



# list_nums = [i for i in range(1, 10,2)]
# # for i in range(1, 10, 2):
# #         list_nums.append(1)

# print(list_nums)



list_names = ['Alex', 'Bob', 'Samuel', 'Sam',]
list_names.sort()
print(list_names)

replased_name = input('Какое имя вы хотите заменить?\n')
name = input('На какое имя вы хотите заменить?\n')
index = list_names.index(replased_name)
list_names.insert(index, name)

print(list_names)



























