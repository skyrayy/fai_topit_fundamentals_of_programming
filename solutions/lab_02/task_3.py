
import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

print('==================================================================')


import weakref

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print('==================================================================')


import weakref

class Record:
    pass

registry = weakref.WeakValueDictionary()

first = Record()
second = Record()
third = Record()

registry['1'] = first
registry['2'] = second
registry['3'] = third

print('До удаления сильных ссылок:')
print(list(registry),'\n')

del third

print('После удаления временной ссылки экземпляра third класса Record:')
print(list(registry),'\n')

del second

print('После удаления временной ссылки экземпляров third и second класса Record:')
print(list(registry),'\n')