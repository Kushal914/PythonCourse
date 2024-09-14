class MyClass:
    x = 10
    _x = 20
    __x = 30

    def get_x(self):
        return self.__x
    
    def fun(self):
        print("Public Function")

    def __fun(self):
        print("Private Function")

obj = MyClass()

# print(obj.x)
# print(obj._x)
# # print(obj.__x)      # gives error
# print(obj.get_x())

obj.__fun()