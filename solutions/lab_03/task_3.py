submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

names = set(name for name, _, _ in submissions)
labs = set(lab for _, lab, _ in submissions)

students_attempts = {}
for name in names:
    students_attempts[name] = []
for name, lab, res in submissions:
    students_attempts[name].append((lab,res))


best_res = {}
for x in submissions:
    key = (x[0], x[1])
    if key not in best_res:
        best_res[key] = x[2]
    else:
        best_res[key] = max(best_res[key], x[2])

labs_attempts = {}
for x in submissions:
    key = (x[0],x[1])
    if key not in labs_attempts:
        labs_attempts[key] = 1
    else:
        labs_attempts[key] += 1

for name in names:
    if (name,'lab_01') in best_res and (name,'lab_02') in best_res:
        print(name)

#==================================================================

submissions.append(("alex", "lab_02", 3))
names.add("alex")
labs.add("lab_02")
students_attempts["alex"] = [("lab_02", 3)]
best_res[("alex", "lab_02")] = 3
labs_attempts[("alex", "lab_02")] = 1

#==================================================================

while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    atr = ['','','']
    blocks = command.split()
    atrs = len(blocks)
    if atrs > 3 or atrs < 1:
        print("Command isn't valid")
        continue
    try:
        atr[0] = blocks[0]
        atr[1] = blocks[1]
        atr[2] = blocks[2]
    except IndexError:
        pass
    if atr[0] == 'exit':
        print('The programm was stopped')
        break
    elif atr[0] == 'student':
        if atr[1] in names:
            print(f'Student {atr[1]} has {students_attempts[atr[1]]} attempts: {', '.join([f'{x[0]}(points: {x[1]})' for x in students_attempts[atr[1]]])}')
        else:
            print(f'Student {atr[1]} not found')
        continue
    elif atr[0] == 'best':
        if (atr[1],atr[2]) in best_res:
            print(f'Best result for {atr[1]} in {atr[2]} is {best_res[(atr[1],atr[2])]}')
        else:
            print(f'No best result for {atr[1]} in {atr[2]}')
        continue
    elif atr[0] == 'attempts':
        if (atr[1],atr[2]) in labs_attempts:
            print(f'{atr[1]} has {labs_attempts[(atr[1],atr[2])]} attempts to submit {atr[2]}')
        else:
            print(f'No attempts for {atr[1]} to submit {atr[2]}')
        continue
    elif atr[0] == 'completed':
        if atr[1] in labs:
            print(f'{atr[1]} was completed by: {', '.join([x for x in names if (x,atr[1]) in best_res])}')
        else:
            print(f'Work {atr[1]} not found')
        continue
    else:
        print(f'Command {atr[0]} not found')
        continue
