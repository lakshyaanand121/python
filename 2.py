# arthametic +,-,*,/,//(integer division),%,**
# relational >,<,<=,>=,==
# logical and,or,not
# bitwise &,|,^(x-or),~(not)
# assignment =
# membership in,not in


# number=int(input('enter number'))
# print(number)
# a=number%10
# number=number//10
# b=number%10
# number=number//10
# c=number
# print(a+b+c)


# email1='lakshya'
# pas1=12345
# email2=input('enter email')
# pas2=int(input('enter pass'))
# if email1==email2 and pas1==pas2:
#     print("verified")
# elif email1==email2 and pas1!=pas2:
#   print('password incorrect')
#   pas2=int(input('enter password again'))
#   if pas1==pas2:
#      print('correct')
#   else:
#      print("u can't")   
# else:
#     print("wrong email or pass")    


# a=int(input('enter number first  '))
# b=int(input('enter number second  '))
# c=int(input('enter number third  '))
# 
# if a<b and a<c:
#     print('a is smallest')
# elif b<a and b<c:
#     print('b is smallest')
# else:
#     print('c is smallest')      


# num1=int(input('enter first number: '))
# num2=int(input('enter second number: '))
# 
# operation=input('enter operation +,-,*,/ :  ')
# 
# if operation=='+':
#     print(num1+num2)
# elif operation=='-':
#     print(num1-num2)
# elif operation=='*':
#     print(num1*num2)
# elif operation=='/':
#     print(num1/num2)            
# else:
#     print('invalid operation')  


# modules:
#math
import math
print(math.factorial(3))
#keyword
import keyword
print(keyword.kwlist)
#random
import random
print(random.randint(1,100))
#datetime
import datetime
print(datetime.datetime.now())

help('modules')