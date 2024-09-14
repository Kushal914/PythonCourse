marks = []

def get_info():
    global name, age
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    
    with open('student.txt', 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

def get_marks():
    global no_of_sub
    no_of_sub = int(input("Enter the no of subjects: "))

    with open('student.txt', 'a') as file:
        file.write("Marks obtained in:\n")
    
    for i in range(no_of_sub):
        value = int(input(f"Enter the marks obtained in sub.{i + 1}: "))
        marks.append(value)
        with open('student.txt','a') as file:
            file.write(f"Sub.{i + 1}: {value}\n")

def get_result():
    total_marks = 0.0
    for i in range(no_of_sub):
        total_marks += marks[i]
    global gpa
    gpa = total_marks / (no_of_sub * 100) * 4.0
    with open('student.txt','a') as file:
        file.write(f"Total Marks: {total_marks}\n")
        file.write(f"GPA: {gpa}\n")

# def show_results():
#     print(f"The results of {name} is {marks}, gpa is {gpa}")

def update_file():
    get_info()
    get_marks()
    get_result()
    with open('student.txt', 'a') as file:
        file.write("\n")
    print("Update Successful")

def read_file():
    with open('student.txt', 'r') as file:
        print(file.read())

print("Select:")
print("1. Update file")
print("2. Read file")
choice = int(input())

if choice == 1:
    update_file()
elif choice == 2:
    read_file()
else:
    print("Invalid choice")