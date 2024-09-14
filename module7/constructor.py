class Human:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__ (self):
        return f'{self.name}, {self.age}, {self.gender}'
        # does not work
        # human_data = {
        #     'name' : self.name,
        #     'age' : self.age,
        #     'gender' : self.gender
        # }
        # return human_data

    # Python does not support constructor overloading
    # def __init__ (self, name):
    #     self.name = name
    #     self.age = 0
    #     self.gender = 'male'

    def check_vote(self):
        if self.age >= 18:
            print(f"{self.name} can vote")
        else:
            print(f"{self.name} cannot vote")

h1 = Human('Kushal', 24, 'male')
h2 = Human('Pawan', 25, 'male')
h3 = Human('Ashish', 10, 'male')

def can_vote(Human):
    if Human.age >= 18:
        print(f"{Human.name} can vote")
    else:
        print(f"{Human.name} cannot vote")

#print(h3.age)
# h1.check_vote()
# h3.check_vote()
# can_vote(h2)

print(h1)