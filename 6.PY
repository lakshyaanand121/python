# 1.Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

# A=int(input('enter angle A: '))
# B=int(input('enter angle B: '))
# C=int(input('enter angle C: '))
# 
# sum=A+B+C
# 
# if sum==180:
#     print('triangle can be form')
# else:
#     print('cannot form a triangle')    


# cost_price=int(input('enter cost price: '))
# selling_price=int(input('enter selling price: '))
# 
# if selling_price>cost_price:
#     print('profit')
# else:
#     print('loss')    


num=int(input('enter number: '))
print("1= cm to ft")
print("2=km to miles")
print("3=USD to INR")
print("4=exit")

opt=int(input('enter option: '))

if opt==1:
    print('cm to ft')
    print('cm =',num,'is ft=',num*0.394)

elif opt==2:
    print('km to miles')
    print('km =',num,'is miles=',num*0.621)

elif opt==3:
    print('USD to INR')
    print('USD =',num,'is INR=',num*94.96)

elif opt==4:
    print('exit')

else:
    print('invalid option')        
