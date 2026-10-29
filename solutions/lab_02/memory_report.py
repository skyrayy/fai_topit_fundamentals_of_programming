import sys,tracemalloc

#Часть 1
results1 = []
results1.append({
    'name' : 'пустой список',
    'obj' : [],
    'length' : 0
})
results1.append({
    'name' : 'список из десяти целых чисел',
    'obj' : [0,1,2,3,4,5,6,7,8,9],
    'length' : 10
})
results1.append({
    'name' : 'кортеж из десяти целых чисел',
    'obj' : (0,1,2,3,4,5,6,7,8,9),
    'length' : 10
})
results1.append({
    'name' :'строка из десяти символов',
    'obj' : '0123456789',
    'length' : 10
})
results1.append({
    'name' : 'целое число',
    'obj' : 10,
    'length' : None
})
results1.append({
    'name' : 'объект None',
    'obj' : None,
    'length' : None
})
for d in results1:
    d['size'] = sys.getsizeof(d['obj'])

#Часть 2
results2 = []
my_list = []
my_list_size = sys.getsizeof(my_list)
k = 0
for x in range(100):
    my_list.append(x)
    if my_list_size != sys.getsizeof(my_list):
        k += 1
        my_list_size = sys.getsizeof(my_list)
        results2.append((x,k,my_list_size))

#Часть 3
results3 = []
results3.append({
    'method' : 'numbers = list(range(100_000))'
})
results3.append({
    'method' : 'numbers = range(100_000)'
})

tracemalloc.start()
numbers = list(range(100_000))
current1, peak1 = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
numbers = range(100_000)
current2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()

results3[0]['current'] = current1
results3[0]['peak'] = peak1
results3[1]['current'] = current2
results3[1]['peak'] = peak2

#Вывод
print('===== Часть 1. Размер отдельных объектов =====\n')
for i in results1:
    print(f'объект: {i['name']}\nэлементов: {i['length']}\nразмер: {i['size']} байт\n')
print('-----------------------------------------------')
print('===== Часть 2. Рост списка =====\n')
for i in results2:
    print(f'добавленный элемент: {i[0]}\nномер изменения:{i[1]}\nразмер: {i[2]}\n')
print('-----------------------------------------------')
print('===== Часть 3. Измерение через tracemalloc =====\n')
for i in results3:
    print(f'метод: {i['method']}\nтекущий объем: {i['current']/1024:.2f} килобайт\nпиковый объем: {i['peak']/1024:.2f} килобайт\n')