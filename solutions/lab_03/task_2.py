import time,tracemalloc
def time_usage(func):
  def wrapper(*args, **kwargs):
    time_start = time.perf_counter()

    result = func(*args, **kwargs)

    print(f"Time to solve: {((time.perf_counter() - time_start)*1000):.3f} ms")

    return result

  return wrapper

def look_through(the_list:list):
    sum = 0 # Сумма всех элементов массива (до подсчета равна нулю)
    min = float('inf') # Минимальный элемент (для первого сравнения берется бесконечность)
    max = float('-inf') # Максимальный элемент (для первого сравнения берется минус бесконечность)
    even = 0 # Счетчик четных чисел
    for current in the_list:
        sum += current # К сумме пройденных элементов прибавляется текущий
        if current < min: min = current # Если текущий элемент меньше минимального, текущий становится минимальным
        if current > max: max = current # Если текущий элемент больше максимального, текущий становится максимальным
        if current % 2 == 0: even += 1 # Если число четное, счетчик увеличивается на 1

    print(f'Сумма элементов: {sum}')
    print(f'Минимальный элемент: {min}')
    print(f'Максимальный элемент: {max}')
    print(f'Четных чисел в списке: {even}')

    mid = sum / len(the_list) # Среднее арифметическое
    excmid = 0 # Счетчик элементов, которые больше, чем mid
    for current in the_list:
        if current > mid: excmid += 1 # Если текущий элемент больше, чем mid, счетчик увеличивается на 1

    print(f'Значений, превосходящих среднее арифметическое: {excmid}')

@time_usage
def look_for(num:int,the_list:list):
    count = 0
    for idx in range(len(the_list)):
        count += 1
        if the_list[idx] == num:
            print(f'Число {num} соответствует элементу с индексом {idx}') # Выводит ТОЛЬКО индекс первого вхождения в список. Повторные вхождения не учитываются.
            return idx, count
    else:
        return -1, count


def is_prime(num:int):
    for i in range(2,int((num)**0.5+1)):
        if (num == 1) or (num > 3 and num % i == 0): 
            print(f'Число {num} - не простое')
            break
    else:
        print(f'Число {num} - простое')

def selection_sort(the_list:list):
    count = 0
    cur_idx = 0
    while cur_idx < len(the_list) - 1 :
        min_idx = cur_idx
        for i in range(cur_idx,len(the_list)):
            count += 1
            if the_list[i] < the_list[min_idx]: min_idx = i
        the_list[cur_idx], the_list[min_idx] = the_list[min_idx], the_list[cur_idx]
        cur_idx += 1
    return the_list, count

@time_usage
def bin_search(num:int,the_list:list):
    count = 0
    left = 0 
    right = len(the_list) - 1
    n = (left + right) // 2
    while left <= right:
        count += 1
        if the_list[n] == num: return n, count
        elif the_list[n] > num: right = n - 1
        else: left = n + 1
        n = (left + right) // 2
    return -1, count

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

print("1. Анализ списка")
look_through(measurements)
print("Временная сложность: O(n)")
print('\n')

print("2. Линейный поиск первого вхождения числа в список")
target = int(input('Введите число: '))
look_for(target,measurements)
print("Временная сложность: O(n)")
print('\n')

print("3. Проверка простоты числа")
checked = int(input('Введите число: '))
is_prime(checked)
print("Временная сложность: O(n^0.5)")
print('\n')

with open('input_100.txt', 'r') as f:
    first = list(map(int, f.read().split()))

with open('input_1000.txt', 'r') as f:
    second = list(map(int, f.read().split()))

with open('input_10000.txt', 'r') as f:
    third = list(map(int, f.read().split()))

print('===== Линейный поиск =====')
print('----- n = 100 -----')
print(look_for(15,first))
print('----- n = 1000 -----')
print(look_for(15,second))
print('----- n = 10000 -----')
print(look_for(15,third))

print('\n===== Бинарный поиск =====')
print('----- n = 100 -----')
print(bin_search(15,first))
print('----- n = 1000 -----')
print(bin_search(15,second))
print('----- n = 10000 -----')
print(bin_search(15,third))
