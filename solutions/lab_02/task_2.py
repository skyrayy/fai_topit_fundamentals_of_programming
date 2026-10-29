import copy

def lists_description(a:list,b:list,c:list,d:list):
    print('Исходные объекты:')
    print(a,', id: ',id(a),sep='')
    print(b,', id: ',id(b),sep='')
    print(c,', id: ',id(c),sep='')
    print(d,', id: ',id(d),sep='')

    print('Первые вложенные списки:')
    print(a[0],', id: ',id(a[0]),sep='')
    print(b[0],', id: ',id(b[0]),sep='')
    print(c[0],', id: ',id(c[0]),sep='')
    print(d[0],', id: ',id(d[0]),sep='')

    print('Объекты с первой оценкой:')
    print(a[0][1],', id: ',id(a[0]),sep='')
    print(b[0][1],', id: ',id(b[0]),sep='')
    print(c[0][1],', id: ',id(c[0]),sep='')
    print(d[0][1],', id: ',id(d[0]),sep='')
    print('=================================================')

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

#Изменения:
#1
original.append(["Databases", 5])
lists_description(original,alias,shallow,deep)

#2
original[0][1] = 3
lists_description(original,alias,shallow,deep)

print('==================================================================')

wrong_matrix = [[0] * 3] * 3
print(wrong_matrix)

wrong_matrix[0][0] = 1
print(wrong_matrix)

print(wrong_matrix[0] is wrong_matrix[1])
print(wrong_matrix[1] is wrong_matrix[2])
print(wrong_matrix[2] is wrong_matrix[0])


correct_matrix = [[0] * 3 for _ in range(3)]
print(correct_matrix)

correct_matrix[0][0] = 1
print(correct_matrix)

print(correct_matrix[0] is correct_matrix[1])
print(correct_matrix[1] is correct_matrix[2])
print(correct_matrix[2] is correct_matrix[0])