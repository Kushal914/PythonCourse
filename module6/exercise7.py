students = {}
highest_marks = 0
topper = ''

for i in range(5):
    name = input("Enter student's name: ")
    print("Enter marks obtained in")
    maths = int(input("Maths: "))
    science = int(input("Science: "))
    english = int(input("English: "))
    marks = {'maths' : maths, 'science' : science, 'english' : english}
    students[name] = marks

for std in students:
    total_marks = 0
    for sub in students[std]:
        total_marks += students[std][sub]
    print(f"Total Marks by {std} is {total_marks}.")

    if total_marks > highest_marks:
        highest_marks = total_marks
        topper = std

print(f"The topper is {topper} with {highest_marks} marks.")