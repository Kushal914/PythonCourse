Text = "How are you?"

with open('myfile.txt', 'w') as file:
    file.write(Text)

print("Writing Success")