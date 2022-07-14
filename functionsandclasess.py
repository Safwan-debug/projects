'''print('hello')'''
student={
'name':'safwan',
'branch':'eee',
'batch':'2020',
}

'''print(student.items())'''
'''for show,saf in student.items():
    print(student.get(show))'''
    
'''for k in range(1,10):
    print(k)'''

'''for j,k in student.items():
    print(student.get(k))'''
    
'''for i in range(20,30):
    print(i)'''
    
#list compensation
'''for j in range(1,10):
    print(j)'''
'''output=[j for j in range(1,10)]
print(output)'''

'''for i in range(1,10):
    if i%3==0:
        print(i)'''  
'''o=[j for j in range(30,40) if j%3==0]
prin'''

'''for i in range(1,10): # doubt
    if i%2==0:
        print(i)
    else:
     print(100)'''    
     
'''saf1=[i if i%2==0 else 'odd' for i in range(1,10)]
print(saf1)''' 

'''x=200
while(x>10):
    print(x)
    x=x-50'''
     
'''x=500
while(x>10):
    print(x)
    x=x-50'''
    
'''show=700
while(show>=50):
    print(show)
    show=show-200'''
    
#function
'''def saf():  #define
    print('\n')
    print('**********************')
    print('\n')
    
saf()
print('i am safwan')  #driven 
saf()
print(' am from shimoga')'''

'''def p(h):
    print('\n')
    for i in range(h):
        print(i)
        if i%2==0:
            print('********************')
            print('\n')
     
        else:
            print('hi')
    
p(4)
print('i am safwan')
p(2)

def cube(x):
    return x**3'''
    
''''print(cube(2))'''

'''def operater(power):
    return lambda number:number**power
cube=operater(2)
print( cube(3)) '''

'''def joke(exponetial):
    return lambda number:number**exponetial
hexa=joke(3)
print(hexa(2))'''    

'''def saf(power):
    return lambda number : number**power
four=saf(4)
print(four(10))''' 

#fibinochi series 
'''def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)       
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(a+b)
fib(10)''' 

#palendrome or not 
'''def palandrome(j):
    return j == j[::-1]     
    
j='byb'
ans=palandrome(j)
if ans:
    print('yes')
else:
    print('no')'''

#factorial of number 5!
def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f

n=4
'''result=fact(n)
print(result)'''

#armstrong number    #371,407,153,370
'''num=input('enter number')
sum=0
for i in num:
    sum+=int(i)**3
if sum==int(num):
    print('armstrong')
else:
    print('not armstrong')'''

#patterns matching programe 
'''for i in range(4):
    for j in range(4-i):
        print('#',end='')
    print()'''         
    
'''for i in range(4):
    for j in range(4):
        print('#',end='')
    print()'''

#prime number or not in python 
'''l=3
for i in range(2,l):
    if l%i==0:
        print('not a prime number')
        break
else:
    print('its a prime number')'''

#programe to riverse a list  
'''g=[1,3,4,'fgdg',7,'ieue']
g.reverse()
print('reversed lis ==>',g)''' 