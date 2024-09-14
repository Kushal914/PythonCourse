class Parent:
    def fun(self):
        print("Public Function")

    def __fun(self):
        print("Private Function")

class Child(Parent):
    def call_public(self):
        self.fun()

    def call_private(self):
        self.__fun()

obj = Child()

obj.call_private()