# n:int=5
# name:str="lakshya"
# print(type(n))
# print(n)
# 
# def sum(a:int,b:int):
#     return a+b
# print(sum(7,5))

# from typing import list,union ,Tuple
# person:list(int)=[1,2,3,4,5]
# person2:dict(str,int)={"lakshya":19,"shyam":20}
# password:union(str,int)="lak123"

# def http_status(status):
#     match status:
#         case 200:
#             return 'ok'
#         case 404:
#             return 'not found'
#         case 500:
#             return 'internal server error'
#         case _:
#            return 'unknown status'
# 
# print(http_status(200))     
# print(http_status(404))   
# print(http_status(500))  
# print(http_status(456))          

# dict1={'lakshya':19}
# dict2={'qwerqw':123}
# merged=dict1|dict2
# print(merged)

# try:
#     a=int(input('enter number: '))
#     print(a)
# except:
#     print('invalid number')    
try:
    with open('file1.txt','r')as f:
        print(f.read())

except Exception as e:
    print(e)
    
try:  
    with open('file.txt','r')as f:
        print(f.read())

except Exception as e:
    print(e)
        
try:
    with open('file2.txt','r')as f:
        print(f.read())

except Exception as e:
    print(e)

print('thank u')                    