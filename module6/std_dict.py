import csv

marks = []

def get_info():
    global name, age
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))

def get_marks():
    global no_of_sub
    no_of_sub = int(input("Enter the no of subjects: "))
    
    for i in range(no_of_sub):
        value = int(input(f"Enter the marks obtained in sub.{i + 1}: "))
        marks.append(value)

def get_result():
    global total_marks, gpa
    total_marks = 0.0

    for i in range(no_of_sub):
        total_marks += marks[i]

    gpa = total_marks / (no_of_sub * 100) * 4.0

# def show_results():
#     print(f"The results of {name} is {marks}, gpa is {gpa}")

def update_file():
    get_info()
    get_marks()
    get_result()

    student = [{
            'name' : name,
            'age' : age,
            'gpa' : gpa,
            'total_marks' : total_marks
    }]

    header = ['name', 'age', 'gpa', 'total_marks']

    for i in range(no_of_sub):
        student[0][f'sub{i+1}'] = marks[i]
        header.append(f'sub{i+1}')

    with open('std_data.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames = header)
        #writer.writeheader()
        writer.writerows(student)

def read_file():
    with open('std_data.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter = ',')
        for row in reader:
            print(row)

def read_file_above_15():
    with open('std_data.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter = ',')
        for row in reader:
            if int(row['age']) > 15:
                print(row)

def run():
    print("Select:")
    print("1. Update file")
    print("2. Read file")
    print("3. Show info of students above the age of 15")
    print("0. Exit")
    choice = int(input())

    if (choice != 0):
        if choice == 1:
            update_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            read_file_above_15()
        else:
            print("Invalid choice")
        run()
    else:
        print("Program exited")

run()