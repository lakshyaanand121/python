# num=int(input('enter number: '))
# result=0
# fact=1
# for i in range(1,num+1):
#     fact=fact * i
#     result=(result+i)/fact
# 
# print(result)  

# nested loop

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j) 

# rows=int(input('number of rows: '))
# 
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()        

# rows=int(input('enter rows: '))
# for i in range(1,rows+1):
#    for j in range(1,i+1):
#       print(j,end=' ')
#    for k in range(i-1,0,-1):
#       print(k,end=' ') 
#    print()      

upper=int(input('enter upper: '))
lower=int(input('enter lower: '))

for i in range(lower,upper+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)        