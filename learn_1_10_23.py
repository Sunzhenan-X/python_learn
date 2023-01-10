#初学python的第一天2023年1月9日
# print("hello world")
# print('hello world')
# print('hello'\
#       'world')
# print("he say 'hello world'")
# print('he say \'hello world\'')
# name=input('please input you name:')
# print(name)
# print('use print to debug')
#程序员要学会怎么使用注释，并且注释上你这行代码是干什么的
#比如你要调用代码的时候注释清楚你调用的目的是什么，方便去改代码
#ctrl+/可以注释很多行
# first_name='sun'
# last_name='zhenan'
# print('hello'+' '+first_name+' '+last_name)通常使用'+'来进行字符的拼接
#下面是一些常用方法
'''
print('hello'.upper())#全部大写
print('fuck'.lower())#全部小写
print('ohhhhh'.capitalize())#首字母大写
print('attention'.count('t'))#表明你所输入字母出现的次数
'''
# 下面都是关于字符串的实操
# first_name=input('please input your first_name:')
# last_name=input('please input your last_name')
# print('hello'+' '+first_name.capitalize()+last_name.capitalize()+' ''welcome'\
#       "I've glad to see you!")

# ok我们现在已经学会了如何使用字符串，那我们现在来尝试一下去使用格式化字符串format
'''
first_name=input('please input your first_name:')
last_name=input('please input your last_name')
output='hello'+' '+first_name+''+last_name
output_1=f'hello,{first_name}{last_name}'#这个比较常用
output_2='hello,{}{}'.format(first_name,last_name)#这个方法和下面那个差不多，都是看排序，不过重要的一点是排序从0开始
output_3='hello,{0}{1}'.format(first_name,last_name)
print(output)
print(output_1)
print(output_2)
print(output_3)
'''
#ok我们现在已经学会了如何使用字符串，那么我们现在来学习一下python中的数字
#和字符串一样我们依然可以在变量中储存数字
#一些常见的数字运算符：+加法 -减法 /除法 *乘法 **指数（下面是实操一波）
# first_number=24
# second_number=8
# answer_1=first_number+second_number
# answer_2=first_number-second_number
# answer_3=first_number*second_number
# answer_4=first_number**second_number
# answer_5=first_number/second_number
# print(answer_1)
# print(answer_2)
# print(answer_3)
# print(answer_4)
# print(answer_5)#是浮点数

#当你开始使用数字时你通常会遇到不同的数字类型，像数字类型其实是字符串类型，即python不支持int类型和string类型使用‘+’
#即我们只能数字+数字，或者字符串+字符串，那么当我们遇到不对等的情况我们就需要类型转换
#将数字类型转化为字符串则使用字符串函数str()，转化为整型是int(),转化为浮点型是float(),所以在涉及到数字时，用好数据转换
'''
day=22
print(str(day)+''+'days in April')
#也可以这样
day='22'
print(day+' '+'days in April')
#还可以将数字表示为字符串，则就可以进行字符串的基本操作，拼接字符,
num_1='1'
num_2='6'
print(num_1+num_2)
num_3=input('please enter a number:')
num_4=input('please enter a number:')
print(num_3+num_4)#要注意是拼接，不是加减运算
print(int(num_3)+int(num_4))#如果将字符串转为整型，则加减运算正常运行
print(float(num_4)+float(num_3))#和上面同理，将其转化为浮点型，计算正常
'''
#ok我们现在已经学习了字符串和数字，那么我们接下来学习一下日期
#在这里我们需要用到datetime库调用当前时间,而timedelta这个库是用来看时间间隔的
'''
from datetime import datetime, timedelta #记住了奥，这是从库调用函数的格式捏
current_date=datetime.now()#.now是当前时刻，还有.day和.month和.year
print("what's day is Today?"+'\n'+'The day is'+str(current_date))
one_day=timedelta(days=2)
The_day_befor_yestday=current_date-one_day
print(The_day_befor_yestday)
one_days=timedelta(weeks=1)
last_week=current_date-one_days
print(last_week)
birthday=input('When is your birthday:(dd/mm/yyyy)?')
birthday_date=datetime.strptime(birthday,'%d/%m/%Y')#要注意这里的y要大写！！！！年、月、日：%y、%m、%d   
 #对于年，四位数的格式是大写的%Y,小写的%y市两位数的年，如99年
print('Birthday:'+str(birthday_date))
'''







