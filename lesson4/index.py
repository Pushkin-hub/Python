tup = (1,)
print(type(tup))
list_1 = [1,2]
print(type(list_1))
sett = {1,3, "Hallo"}
print(type(sett))
dictt = {1: 3, 2: "Academy"}
print(type(Dictt))
tup_2 = (1, 4, 4, 90)
print(type(tup_2))
print(dir(tup_2))
print(dir(list_1))

x = 1
print(x)
print(id(x))
x += 1
print(x)
print(id(x))

lst = [1, 90, 87, "WEB"]
print(lst)
print(id(lst))
lst.append("You are a cool!")
print(lst)
print(id(lst))

number_and_words = [1, 1, 5, 7, 9, 9, 'Hello', 'hello']
print(number_and_words)

many = set(number_and_words)
print(many)

y = 1
print(dir(x))
d = str(y)
print(type(d))

st ='123'
num = int(st)
print(type(num))

h = [1, 2, 3]
print(max(h))

new_list = []
old_list = [10, 20, 10, 20, 30, 40, 30, 50]
for i in old_list:
    if i not in new_list:
        new_list.append(i)
print(old_list)
print(new_list)


