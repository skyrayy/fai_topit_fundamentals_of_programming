student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[0], student[3], sep=',')

name = student[:-9]
last_name = student[5:]
print(name, last_name, sep=',')

print(student.upper(), student.lower(), sep=',')

inicials = student[0]+'.'+student[5]+'.'
print(inicials)

print(course[::-1])

result1 = "%s — %s: %d/%d (%.1f%%)" % (name, course, completed, total, (completed/total)*100)
print(result1)

result2 = "{} — {}: {}/{} ({:.1f}%)".format(name, course, completed, total, (completed/total)*100)
print(result2)

result3 = f"{name} — {course}: {completed}/{total} ({(completed/total)*100:.1f}%)"

symbol = "Я"
print(symbol)
print(ord(symbol))
print(chr(ord(symbol))) 
print(symbol.encode('utf-8'))
print(len(symbol.encode('utf-8')))

l='color'
#l[0]='k'