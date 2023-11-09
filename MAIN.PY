def q1():
    def outer_fun(a, b):
        def inner_fun(c, d):
            return c + d

        return inner_fun(a, b)
        return a

    result = outer_fun(5, 10)
    print(result)
def q3():
    def fun1(num):
        return num + 25

    fun1(5)
    #--
    num = fun1(5)
    #--
    print(num)

def q4():
    def outer_fun(a, b):
        def inner_fun(c, d):
            return c + d
        return inner_fun(a, b)

    res = outer_fun(5, 10)
    print(res)

def q6():
    def fun1(name, age=20):
        print(name, age)

    fun1('Emma', 25)
def q7():
    def add(a, b):
        return a+5, b+5

    result = add(3, 2)
    print(result)
def q8():
    def fun1(*data):
        for i in data:
            print(i)
            print("Done!")  
    fun1(25, 75, 55)
    fun1(10, 20)
def q10():
    def display(**kwargs):
        for i in kwargs:
            print(i)

    display(emp="Kelly", salary=9000)
def q12():
    def display_person(*args):
        for i in args:
            print(i)

    display_person(name="Emma", age="25")
    