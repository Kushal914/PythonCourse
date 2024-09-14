class Animal:
    a_value = 10
    def __init__ (self):
        pass
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__ (self):
        pass
    def make_sound(self):
        print ("Dog barks.")

# dog1 = Dog()
# dog1.make_sound()

class Plant():
    p_value = 0

animal1 = Animal()
plant1 = Plant()

plant1.p_value = animal1.a_value

print(plant1.p_value)