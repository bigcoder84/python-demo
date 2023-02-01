class Student(object):
    # 类属性，类似于java 类中的静态属性
    id = "1123123123123"

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


if __name__ == '__main__':
    stu = Student("张三", 80)
    stu.pp = "123"
    stu._Student__name = "王五"
    print(stu._Student__name)
    print(dir(stu))
    print(Student.id)
    stu.print_score()