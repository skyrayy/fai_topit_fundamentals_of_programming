
print('===эксперимент а===')
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))


print('===эксперимент b===')
first = [10, 20]
second = first
second = first.copy()

print(first, second)
print(id(first), id(second))

print(first == second)
print(first is second)

second.append(30)

print(first, second)
print(id(first), id(second))

print('==================================================================')

#ver1
print('Первая версия:')
config1 = {
    'name' : 'Учебный проект',
    'members' : ['Иван Поддубный','Владимир Джанибеков'],
    'parameters' : [10 , 15]
                }

config2 = config1

print('До преобразования:')
print('config1:' , config1)
print('config2:' , config2)
print('identity:' , config1 is config2)


config2['members'].append('Сергей Бондарчук')
config2['parameters'].append(25)
config2['status'] = 'verified'

print('После преобразования:')
print('config1:' , config1)
print('config2:' , config2)
print('identity:' , config1 is config2)


print('=======================================')


#ver2
from copy import deepcopy
print('Вторая версия:')
config1 = {
    'name' : 'Учебный проект',
    'members' : ['Иван Поддубный','Владимир Джанибеков'],
    'parameters' : [10 , 15]
                }

config2 = deepcopy(config1)

print('До преобразования:')
print('config1:' , config1)
print('config2:' , config2)
print('identity:' , config1 is config2)

print('Общие объекты:')
if config1['name'] is config2['name']: print('name: ',config2['name'],sep='')
if config1['members'] is config2['members']: print('members: ',config2['members'],sep='')
if config1['parameters'] is config2['parameters']: print('parameters: ',config2['parameters'],sep='')

config2['members'].append('Сергей Бондарчук')
config2['parameters'].append(25)
config2['status'] = 'verified'

print('После преобразования:')
print('config1:' , config1)
print('config2:' , config2)
print('identity:' , config1 is config2)
assert config1 is not config2, 'конфигурации связаны'
