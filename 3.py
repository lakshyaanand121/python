# num=int(input('enter the number: '))
# i=1
# while i<11:
#     print(num,'*',i,'=',num*i)
#     i+=1

# x=1
# while x<3:
#     print(x)
#     x+=1
# else:
#     print('end')  

# import random
# jackpot=random.randint(1,10)
# 
# guess=int(input('enter guess: '))
# count=1
# while guess!=jackpot:
#     if guess<jackpot:
#         print('guess higher')
#     else:
#         print('guess lower')
#     
#     guess=int(input('guess again'))
#     count+=1
# else:
#     print('correct guess')
#     print('attempts: ')  

# for loop

# for i in range(1,11):
#     print(i)
# for j in range(10,0,-1):
#     print(j)

current_pop=10000

for i in range(10,0,-1):
    print(i,current_pop)
    current_pop=current_pop-0.1*current_pop