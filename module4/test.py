marks = []

def get_info():
    global name, age
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))

def get_marks():
    global no_of_subj
    no_of_subj = int(input("Enter the number of subjects: "))
    for i in range(no_of_subj):
        value = int(input(f"Enter the marks obtained in subj. {i + 1}: "))
        marks.append(value)

def get_result():
    total_marks = 0.0
    for i in range(no_of_subj):
        total_marks += marks[i]
    global gpa
    gpa = total_marks / (no_of_subj * 100) * 4.0

def show_results():
    print(f"The results of {name} is {marks}, gpa is {gpa}")

get_info()
get_marks()
get_result()
show_results()


# num = int(input("Enter an integer: "))
# print(f"Multiplication table of {num}")
# for i in range (1, 11):
#     print(f"{num} * {i} = {num * i}")