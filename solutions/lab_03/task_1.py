def diap(x:int,min:int,max:int): # Проверка на вхождение в диапазон
    return min <= x <= max

def level(result:int,absent:int): 
    if 90 <= result <=100: lvl = 4 # Определение уровня по баллу
    elif 75 <= result <= 89: lvl = 3
    elif 60 <= result <= 74: lvl = 2
    else: lvl = 1
    
    if lvl != 1 and absent > 3: lvl -= 1 # Если уровень позволяет, снижаем его за множественные пропуски
    
    return lvl

def conc(conclusion:dict,name:str): # Итог по типу работы
    print(f'        Работ уровня Отличный: {conclusion[name][2]}')  
    print(f'        Работ уровня Хороший: {conclusion[name][3]}')  
    print(f'        Работ уровня Удовлетворительный: {conclusion[name][4]}')  
    print(f'        Работ уровня Недостаточный: {conclusion[name][5]}') 
    if conclusion[name][0] != 0:
        print(f'    Средний балл: {(conclusion[name][1]/conclusion[name][0]):.2f}')
    else:   
        print(f'    Средний балл: {(conclusion[name][1]):.2f}')

def analysing(db:list): # Итоговая программа. db - список кортежей

    conclusion = {'exam' : [0,0,0,0,0,0],   # Словарь для итоговой сводки
                  'project' : [0,0,0,0,0,0], # Что означают элементы вложенных списков: [count, sum_score, lvl=4, lvl=3, lvl=2, lvl=1]
                  'practice' : [0,0,0,0,0,0]}

    lvl_name = {1 : 'Недостаточный',
                2 : 'Удовлетворительный',
                3 : 'Хороший',
                4 : 'Отличный'}
    
    for id in range(len(db)):

        i = db[id]
        result , name , absent = i[0] , i[1] , i[2]

        print(f'------------------------------')
        if not (diap(result,0,100) and diap(absent,0,5)):
            print(f'id: {id}')
            print('Данные введены некорректно.\n')
        
        else:

            lvl = level(result,absent)

            match name:
                case 'exam': 
                    worktype = 'Экзаменационная работа'                  
                case 'project': 
                    worktype = 'Проектная работа'             
                case 'practice': 
                    worktype = 'Практическая работа'                   
                case _: 
                    worktype = 'Не указан'

            if worktype != 'Не указан':

                conclusion[name][0] += 1
                conclusion[name][1] += result  

                if lvl == 4: 
                    conclusion[name][2] += 1
                elif lvl == 3: 
                    conclusion[name][3] += 1
                elif lvl == 2: 
                    conclusion[name][4] += 1
                else: 
                    conclusion[name][5] += 1  

            print(f'id: {id}')
            print(f'Тип работы: {worktype}')
            print(f'Результат: {result} из 100')
            print(f'Уровень: {lvl_name[lvl]}')      
        print(f'------------------------------')


    print(f'------Итоговая сводка------')

    print(f'Всего работ сдано: {len(db)}')
    name = 'exam'
    print(f'    Экзаменационных: {conclusion["exam"][0]}') 
    conc(conclusion,name)

    name = 'project'
    print(f'    Проектных: {conclusion["project"][0]}')
    conc(conclusion,name)

    name = 'practice'
    print(f'    Практических: {conclusion["practice"][0]}')
    conc(conclusion,name)

# Дальше тестируем

test_db = [
    (95, 'exam', 1),       # 0
    (90, 'project', 0),    # 1. Граница 90 (должен быть отличный)
    (89, 'practice', 2),   # 2. Граница 89 (должен быть хороший)
    (75, 'exam', 2),       # 3. Граница 75 (должен быть хороший)
    (74, 'project', 3),    # 4. Граница 74, пропусков ровно 3 (уровень удовлетворительный, не падает)
    (60, 'practice', 5),   # 5. Граница 60, пропусков > 3 (уровень упадет с удовлетворительного на недостаточный)
    (59, 'exam', 4),       # 6. Граница 59, пропусков > 3 (уровень уже недостаточный, ниже упасть не может)
    (0, 'project', 2),     # 7. Граница 0
    (100, 'practice', 1),  # 8. Граница 100
    (105, 'exam', 1),      # 9. Некорректный ввод score > 100
    (80, 'project', 6),    # 10. Некорректный ввод absences > 5
    (85, 'essay', 2),      # 11. Неизвестный тип работы
]

analysing(test_db)