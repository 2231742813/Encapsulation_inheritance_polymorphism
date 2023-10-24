
class Test:
    def __init__(self,name='默认名称'):
        self.__name = name

    @property
    def name(self):
        return self.__name
        # print(self.name)

    @name.setter
    def name(self, value) :
        self.__name = value


# obj = Test()
# print(obj.name)

Test().name = '123'
print(Test().name)