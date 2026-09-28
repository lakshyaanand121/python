# class addition:
#     def setdata(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print('sum is : ',self.a+self.b)
# a1=addition()
# a1.setdata(10,20)
# s=a1.add()
# print(s)

# class addition:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print('constructor called')
#     def add(self):
#         return self.a + self.b
#     def __del__(self):
#         print('destructor called')
# a1=addition(10,20)
# print(a1.add())        
# del a1

# class year:
#     def yr(self):
#         print('2nd year')
# class branch:
#     def brn(self):
#         print('AI/DS')
# class section:
#     def sec(self):
#         print('B')
# class student(year,branch,section):
#     print('lakshya anand')
# s=student()
# s.yr()
# s.brn()                           
# s.sec()

# for i in range(1,11):
#     if(i==5):
#         break
#     print(i)
# 
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)   


# num=3
# for i in range(1,11):
#     print(i*num)


# start=1
# last=5
# sum=0
# for i in range(start,last+1):
#     sum=sum+i
# print(sum) 

# a=0
# b=1
# total=0
# while(a<=8):
#     print(a)
#     total=total+a
#     a=b
#     b=a+b
# print(total)


# f=open("file.txt")
# data=f.read()
# print(data)
# f.close


# l='lakshya'
# f=open("myfile.txt","w")
# f.write(l)
# f.close

# f=open("file.txt")
# 
# line1=f.readlines()
# print(line1,type(line1))
# 
# line2=f.readlines()
# print(line2,type(line2))
# 
# line3=f.readlines()
# print(line3,type(line3))
# 
# f.close()

# f=open("file.txt")
# content=f.read()
# if("GOAL" in content):
#     print('yes')
# else:
#     print('no')
# f.close()     

