import sys
import tracemalloc

empty_list = []
ten_numbers_list = [x for x in range(10)]
ten_numbers_tuple = tuple(ten_numbers_list)
string = '1'*10
integer = 10
none_obj = None

for x in [empty_list,ten_numbers_list,ten_numbers_tuple,string,integer,none_obj]:
    print('object:',x)
    print('size =',sys.getsizeof(x),'\n')

my_list = []
my_list_size = sys.getsizeof(my_list)
k = 0
for x in range(100):
    my_list.append(x)
    if my_list_size != sys.getsizeof(my_list):
        k += 1
        my_list_size = sys.getsizeof(my_list)
        print(f'append: {x}     change {k}:',my_list_size)


print('     создание numbers = list(range(100_000))')
tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print('---объем памяти---')
print(f'текущий: {current} B = {current / 1024:.2f} Kb    пиковый: {peak} B = {peak / 1024:.2f} Kb')
print('================================')

print('     создание numbers = range(100_000)')
tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print('---объем памяти---')
print(f'текущий: {current} B = {current / 1024:.2f} Kb    пиковый: {peak} B = {peak / 1024:.2f} Kb')