#py学习记录02
"""
收获:
1.函数的声明和调用,以及函数名就是函数地址
2.函数的返回值和参数,以及空返回值None
3.函数的参数的缺省值/默认值
4.函数参数原来可以用指定的方式填值!!!
5.全局变量在函数内只能访问不能更改!!!   （除非加上global关键字指定是全局的那一个）
6.py有一些常用的内置函数
7.py类型转换不能一次转两步,比如不可以这样 int('123.4')
感谢:
https://www.byhy.net/prac/pub/py/0005/
"""


#最简单的函数的声明和调用
"""
def Test_fun_1():
    print("这是一个测试函数")
    print("这是测试函数的第二条语句")

print("尝试调用自定义函数:")
Test_fun_1()
print(Test_fun_1)         #会打印函数地址
"""

#带参数的函数
"""
def Test_fun_2(para1, para2):
    print("接收到参数1: " + str(para1))
    print("接收到参数2: " + str(para2))
    print("相加值:" +str(para1 + para2) )

print("尝试调用自定义函数:")
Test_fun_2(11,12)
"""

#带返回值的函数
"""
def Test_fun_3(para1,para2):
    return (para1 + para2)
    print("return之后的语句不会运行")

print("尝试调用自定义函数:")
print( "Test_fun_3(11,12) = " + str(Test_fun_3(11,12)))
"""

#测试没有return的返回值
"""
def fun_test_4():
    print("自定义函数成功被调用!")

print("尝试调用自定义函数:")
print(fun_test_4())             #和C一样先对fun_test_4()求值，会先运行这个函数，然后拿到返回值再运行print
"""

#函数参数默认值测试
"""
def test_fun_5(para_1, para_2 = 0, para_3 = 0):
    print("para_1 = " + str(para_1))
    print("para_2 = " + str(para_2))
    print("para_3 = " + str(para_3))

print("尝试调用自定义函数:")
test_fun_5(1,2,3)
print("尝试调用自定义函数:")
test_fun_5(1,2)
print("尝试调用自定义函数:")
test_fun_5(1)
"""

#参数指定填写
"""
def Test_fun_6(para_1, para_2 = 0, para_3 = 0, para_4 = 0):
    print("para_1 = " + str(para_1))
    print("para_2 = " + str(para_2))
    print("para_3 = " + str(para_3))
    print("para_4 = " + str(para_4))

print("尝试调用自定义函数:")
Test_fun_6(1,para_4=4,para_3=3)
"""

#全局变量和局部变量测试
"""
count = 0
def Test_fun_7():
    #count += 1     #这一行会报错，说明函数内不能修改全局变量，但可以创建同名变量
    print("in fun 7 count = " + str(count))

def Test_fun_8():
    count = -1
    print("in fun 8 count = " + str(count))

print("尝试调用自定义函数:")
print("count = " + str(count))
Test_fun_7()
Test_fun_8()

count += 1
print("count = " + str(count))
Test_fun_7()
Test_fun_8()
"""

#函数内更改全局变量
"""
count = 0

def Test_fun_9():
    global count        #专门声明这个是全局变量,类似C的extern
    count+= 1

print("尝试调用自定义函数:")
print("count = " + str(count))
Test_fun_9()
print("count = " + str(count))
"""

#内置函数测试

#py不能一次转换两步,比如 int('123.4') 会报错
"""
print( "int('1234') = " + str(int('1234')) )
print( "int(123.4) = " + str(int(123.4)) )
print( "float(111) = " + str(float(111)) )
print( "len('hello') = " + str(len('hello')) )
print( "type('hello') = " + str(type('hello')) )

def test_fun_10():
    print('成功调用函数')

temp = test_fun_10()
print( "return of fun = " + str( temp ) )
print( "type of return = " + str( type(temp) ) )
"""

#练习
"""
def get_name_and_age(str_1 = 'NULL', str_2 = -1):
    name = str_1[-2:]
    age = str_2[-2:]
    ret = name + ":" + age
    return ret

print( get_name_and_age("他的名字是小林","他的年龄是17") )
"""
