# num=int(input('enter number: '))
# if(num%2==0):
#     print(num,'is even')
# else:
#     print(num,'is odd')    

#a=int(input('enter first number: '))
#b=int(input('enter second number: '))
#c=int(input('enter third number: '))
#
#if a>b and a>c:
#    print('a is greater')
#elif b>a and b>c:
#    print('b is greater')
#else:
#    print('c is greater')     
  
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)

#num=int(input('enter number: '))
#fact=1
#for i in range(1,num+1):
#    fact=fact*i
#print(fact)    

# num=int(input('enter number: '))
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)

# num=int(input('enter number: '))
# count=str(num)
# print(len(count))

# num=int(input('enter number: '))
# original=num
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# print('reverse: ',reverse)
# if reverse==original:
#     print('the given number is palindrome')
# else:
#     print('not palindrome')    

# num=int(input('enter number: '))
# a=0
# b=1
# while a<=num:
#     print(a)
#     a,b=b,a+b
# print(a,end=' ')    
       
# num=int(input('enter number: '))
# if num%2!=0 and num%3!=0:
#     print(num,'is prime number')
# else:
#     print(num,'is non-prime')  

# s="lakshya is a good boy"
# #print(s[::-1])
# print('a =',s.count('a'),'e =',s.count('e'),'i =',s.count('i'),'o =',s.count('o'),'u= ',s.count('u'))

# s='aba'
# c_s=s
# s=s[::-1]
# if c_s==s:
#     print('palindrome')
# else:
#     print('not palindrome')    

# s="lakshya is a good boy"
# r=s.replace(' ','')
# print(range)
# r=s.replace(' ','')
# print(len(r))
# print(s.title())

l=[3,4,5,3,6,7,8,6,54,34,55]
# print(max(l))
# print(min(l))
# 
# l.remove(max(l))
# print(max(l))

u=list(set(l))
print(u)