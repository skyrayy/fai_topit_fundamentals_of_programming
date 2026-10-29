import gc
import sys

'''
first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)
print('ссылок на first:',sys.getrefcount(first)-1)
print('ссылок на second:',sys.getrefcount(second)-1)

gc.disable()
print("\nАвтоматический сборщик мусора активен:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистики поколений:")
print('\n'.join(map(str,gc.get_stats())))


first_id = id(first)
second_id = id(second)

del first
del second

def isthere(first_id,second_id):
    isfirstthere = False
    issecondthere = False
    for i in gc.get_objects():
        if isfirstthere == True and issecondthere == True: break
        if id(i) == first_id:
            isfirstthere = True
        if id(i) == second_id:
            issecondthere = True

    print('first существует:',isfirstthere)
    print('second существует:',issecondthere)

print('\n=====до сборки=====')
isthere(first_id,second_id)

print('\n==ручная сборка==')
col = gc.collect()
print('объектов удалено:',col)

print('\n=====после сборки=====')
isthere(first_id,second_id)

gc.enable()
'''
gc.disable()
node_a = {"name": "node_a"}
node_b = {"name": "node_b"}
node_c = {"name": "node_c"}
node_ind = {"name": "node_ind"}

node_a["next"] = [node_b]
node_b["next"] = [node_c]
node_c["next"] = [node_a]

print('=====связи=====')
print(node_a,node_b,node_c,node_ind,sep='\n')
print('---иначе:---')
for i in [node_a,node_b,node_c]:
    print(f'{node_a['name']} ссылается на {node_a['next'][0]['name']}')
print(f'node_ind независимый: {node_ind.get('next','да')}\n')

print('сборка до удаления:',gc.collect())

del node_a, node_b, node_c, i # i ссылается на node_c после for

print('сборка после удаления:',gc.collect())

print('node_ind доступен:','да' if node_ind else 'нет')
gc.enable()