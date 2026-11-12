
def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    return sum(values) / len(values)

def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if name == "":
        return "Имя не может быть пустым"
    name = name.strip()
    name = name.title()
    return name

def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    return f'{prefix} студента {normalize_name(student)} с точностью {precision} зн. после запятой: {arithmetic_mean(results):.{precision}f}'

def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    collected = []
    if lowercase:
        for x in tags:
            if x != '' and x.lower() not in collected:
                collected.append(x.lower())
    else:
        for x in tags:
            if x != '' and x not in collected:
                collected.append(x)
    return tuple(collected)

#================================================================================

# arithmetic_mean()
assert arithmetic_mean([1, 2, 3]) == 2.0
assert arithmetic_mean([1, 2, 3, 4, 5]) == 3.0
assert arithmetic_mean([0]) == 0.0

# normalize_name()
assert normalize_name("   John Doe   ") == "John Doe"
assert normalize_name("") == "Имя не может быть пустым"
assert normalize_name("joHn doe     ") == "John Doe"

# build_report()
assert build_report("John Doe", [1, 2, 3]) == "Результат студента John Doe с точностью 2 зн. после запятой: 2.00"
assert build_report("John Doe", [1, 2, 3], prefix="Средний балл") == "Средний балл студента John Doe с точностью 2 зн. после запятой: 2.00"
assert build_report("John Doe", [1, 2, 3], precision=3) == "Результат студента John Doe с точностью 3 зн. после запятой: 2.000"

# collect_tags()
assert collect_tags("a", "b", "C", "a", "b") == ("a", "b", "c")
assert collect_tags("a", "B", "c", "a", "b", lowercase=False) == ("a", "B", "c", "b")
assert collect_tags("a", "B", "c", "", "b") == ("a", "b", "c")

#=================================================================================

dem11 = collect_tags("a", "B", "c", "", "b") # Корректно - позиционные аргументы приняты, именованные применяются по умолчанию
print(dem11)
dem12 = collect_tags("a", "B", "c", "", "b", lowercase=True) # Тоже корректно - то же самое, что и предыдущий вызов
print(dem12)
dem13 = collect_tags("a", "B", "c", "", "b", lowercase=False) # Корректно, но вывод другой - именнованный аргумент задан через lowercase=False
print(dem13)
try:
    dem14 = collect_tags("a", "B", "c", "", "b", True) # Некорректно - именной аргумент задан как позиционный
    print(dem14)
except:
    print('dem14 is incorrect')
try:
    dem15 = collect_tags("a", "B", "c", "", "b", prefix=True) # Некорректно - попытка задать несуществующий именной аргумент
    print(dem15)
except:
    print('dem15 is incorrect')

#==================================================================================

dem_list = ["a", "B", "c", "", "b"]
dem21 = collect_tags(*dem_list) # Распаковка списка в позиционные аргументы
print(dem21)

dem_dict = {
    "precision" : 0,
    "prefix" : "Новый результат"
}
dem22 = build_report('Pavel', [1, 2, 3], **dem_dict) # Распаковка словаря в именованные аргументы
print(dem22)

#==================================================================================

course = "Math" # GLOBAL

def outer():
    semester = 1  # ENCLOSING
    
    def inner():
        lesson = 5  # LOCAL

        nonlocal semester # Изменяем значение semester из внешней функции
        semester += 1
        
        print(f"Курс: {course}")
        print(f"Семестр: {semester}")
        print(f"Занятие: {lesson}")
    
    inner()
    print(f"Семестр после inner(): {semester}")  # semester изменился, проверяем

outer()

#==================================================================================

def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results

#==================================================================================

def apply_to_results(operation, values: list) -> list:
    result_list = []
    for v in values:
        result_list.append(operation(v))
    return result_list

def make_threshold_checker(threshold: float):
    def checker(value: float) -> bool:
        return value > threshold   
    return checker

# === Демонстрация apply_to_results ===

def square(x: float) -> float:
    return x ** 2

results = [1, 2, 3, 4, 5]
squared = apply_to_results(square, results)             # 1) передаем именованную функцию
print(f"Квадраты чисел {results}: {squared}")

cubed = apply_to_results(lambda x: x ** 3, results)     # 2) передаем lambda функцию
print(f"Кубы чисел {results}: {cubed}")

# === Демонстрация make_threshold_checker ===

check_50 = make_threshold_checker(50)
check_80 = make_threshold_checker(80)
test_values = [45, 55, 75, 85]

print(f"\nПроверка с порогом 50:")
for v in test_values:
    print(f"  {v} > 50? {check_50(v)}")

print(f"\nПроверка с порогом 80:")
for v in test_values:
    print(f"  {v} > 80? {check_80(v)}")

