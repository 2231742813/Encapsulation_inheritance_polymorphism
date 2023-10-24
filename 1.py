# coding:utf-8

class Parents(object):
    __name = "kaka"
    __age = 35
    job = "teacher"

    # @staticmethod
    # def __hobby():
    #     print("pingpong")
    #
    # # 调用私有方法hobby
    # def get_hobby(self):
    #     self.__hobby()

    # 获取年龄
    def get_age(self):
        return self.__age

    # 获取姓名
    def get_name(self):
        return self.__name


if __name__ == "__main__":

    p = Parents()
    # 通过留出来的公有方法进行获取封装好的属性
    print(p.get_name())
    print(p.get_age())

    # # 实例化
    # p = Parents()
    # # 调用封装好的私有属性
    # print(p.name)
    # print(p.__name)

    # p = Parents()
    # # 调用封装好的私有方法
    # p.hobby()
    # # line34, in < module >p.hobby()
    # # AttributeError: 'Parents' object has no attribute


'hobby'

"""
line 28, in <module>
    print(p.name)
AttributeError: 'Parents' object has no attribute 'name'

"""

