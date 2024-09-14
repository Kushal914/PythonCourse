# class Calculator:
#     # def add(self, x, y):
#     #     return x + y
#     def add(self,x,y,z):
#         return x + y + z
    
# calc = Calculator()

# # Python does not support function overloading.
# # print(calc.add(5,10))
# print(calc.add(5,10,15))


class Dog:
    def make_sound(self):
        print("Woof")

class Cat:
    def make_sound(self):
        print("Meow")

dog1 = Dog()
cat1 = Cat()

dog1.make_sound()
cat1.make_sound()