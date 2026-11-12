students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

def mean(values:list[float]) -> float:
    if values:
        return sum(values) / len(values)
    else:
        return 0

def minimum(values:list[float]) -> float:
    if values:
        min = float("inf")
        for value in values:
            if value < min:
                min = value
        return min
    else:
        return 0

def maximum(values:list[float]) -> float:
    if values:
        max = float("-inf")
        for value in values:
            if value > max:
                max = value
        return max
    else:
        return 0

def classify(score: float) -> str:
    if 100 >= score >= 90:
        return "Отлично"
    elif score >= 75:
        return "Хорошо"
    elif score >= 60:
        return "Удовлетворительно"
    elif score >= 0:
        return "Неудовлетворительно"
    else:
        return "Некорректные данные"

def student_summary(name: str, results: list[int]) -> dict:
    report = {
        "name": name,
        "mean": mean(results),
        "category": classify(mean(results)),
        "minimum": minimum(results),
        "maximum": maximum(results),
        "count": len(results)
    }
    return report

def find_top_students(students: dict) -> list[str]:
    best_students = []
    maxsum = 0
    for student in students.keys():
        if mean(students[student]) > maxsum:
            maxsum = mean(students[student])
            best_students = [student]
        elif mean(students[student]) == maxsum:
            best_students.append(student)
    return best_students

def group_summary(students: dict) -> dict:
    all_res = []
    for i in students.values():
        all_res += i

    graduee = {
        "Отлично": 0,
        "Хорошо": 0,
        "Удовлетворительно": 0,
        "Неудовлетворительно": 0
    }
    for student in students.keys():
        graduee[classify(mean(students[student]))] += 1
    
    report = {
        "mean" : mean(all_res),
        "categories" : graduee,
        "top_students" : find_top_students(students)
    }
    return report

def format_report(student_data: dict, group_data: dict) -> str:
    s = ('=== Статистика студентов ===\n')
    for _, report in student_data.items():
        s += (f'{report["name"]}: средний балл - {report["mean"]:.2f}, '
              f'минимум - {report["minimum"]}, '
              f'максимум - {report["maximum"]}, '
              f'категория - {report["category"]}\n')
    s = s + ('\n=== Общая статистика ===')
    s = s + (f'\nСредний балл - {group_data["mean"]}')
    s = s + (f'\nКоличество отличников - {group_data["categories"]["Отлично"]}')
    s = s + (f'\nКоличество хорошистов - {group_data["categories"]["Хорошо"]}')
    s = s + (f'\nКоличество уд. выполнения - {group_data["categories"]["Удовлетворительно"]}')
    s = s + (f'\nКоличество неудов. выполнения - {group_data["categories"]["Неудовлетворительно"]}')
    s = s + (f'\nТоп студенты - {group_data["top_students"]}')
    return s



all_student_data = {}
for name, results in students.items():
    all_student_data[name] = student_summary(name, results)

group_data = group_summary(students)

report = format_report(all_student_data, group_data)
print(report)