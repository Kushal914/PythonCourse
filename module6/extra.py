marks = [100, 100, 100, 100]

no_of_sub = 4

header = ['name', 'age', 'gpa', 'total', 'total_marks']

student = [{
        'name' : 'Kushal',
        'age' : 24,
        'gpa' : 4.0,
        'total_marks' : 400
}]


for i in range(no_of_sub):
    #j = str(i + 1)
    student[0][f'sub.{i+1}'] = marks[i]
    header.append(f'sub.{i+1}')

print(header)
print(student)