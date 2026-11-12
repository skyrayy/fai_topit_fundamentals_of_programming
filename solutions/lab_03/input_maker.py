'''from random import randint

def generate_list(n):
    return [randint(1, 10000) for i in range(n)]

with open('input_100.txt', 'w') as f:
    f.write(' '.join(map(str, sorted(generate_list(100)))))

with open('input_1000.txt', 'w') as f:
    f.write(' '.join(map(str, sorted(generate_list(1000)))))

with open('input_10000.txt', 'w') as f:
    f.write(' '.join(map(str, sorted(generate_list(10000)))))


print('Done')'''

