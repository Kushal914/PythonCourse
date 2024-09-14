students = {}

for i in range(3):
    name = input("Enter student's name: ")
    print("Enter marks obtained in")
    maths = int(input("Maths: "))
    science = int(input("Science: "))
    english = int(input("English: "))
    marks = {'maths' : maths, 'science' : science, 'english' : english}
    students[name] = marks

for std in students:
    is_failed = False
    total_marks = 0
    for sub in students[std]:
        total_marks += students[std][sub]
        if students[std][sub] < 40:
            print(f"{std} has failed in {sub} with {students[std][sub]} marks.")
            is_failed = True
    avg_marks = total_marks / 3

    if(is_failed == False):
        if avg_marks < 50.0:
            print(f"{std} has failed with {avg_marks} percent.")
        else:
            print(f"{std} has passed with {total_marks} total marks and {avg_marks:.2f} percentage")