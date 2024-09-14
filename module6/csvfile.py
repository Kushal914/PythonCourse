import csv

# student = [{
#     'name' : 'Kushal',
#     'class' : 12,
#     'roll' : 17
# },
# {
#     # 'name' : 'Sulav',
#     'roll' : 18,
#     'class' : 12,
#     # 'roll' : 18
#     'name' : 'Sulav',
# }]

# with open('data.csv', 'w') as file:
#     fieldname = ['name', 'class', 'roll']
#     writer = csv.DictWriter(file, fieldnames=fieldname)
#     writer.writeheader()
#     writer.writerows(student)

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter = ',')
    line_count = 0
    for row in reader:
        print(row['name'])
        line_count += 1
    print(line_count)


'''
Ask student information as input and store the in CSV file.
Add age to student.
Make sure the student information input consist of a fucntion to handle job.
List all the students whose age is greater than 15.
'''