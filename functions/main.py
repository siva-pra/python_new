#funtions
'''
def functionname(a):
    print(a)
functionname(1)

output:
1
'''
#orbitary argment:
'''
def functionname(*a):
    print(a)
functionname(1,2,3,4,5,6)

output:
(1, 2, 3, 4, 5, 6)
'''
#keyword argment:
'''
def functionname(**a):
    print(a)
functionname(name="krishna",age=20)

output:
{'name': 'krishna', 'age': 20}
'''
#return:
'''
def functionname(a,b):
    return(a+b)
s=functionname(1,2)
print(s)

output:
3

def functionname(a):
    return(a*2)
s=functionname(2)
print(s)

output:
4

def functionname(a):
    for i in a:
        print(i)
functionname([1,2,3,4,])

output:
1
2
3
4  
'''