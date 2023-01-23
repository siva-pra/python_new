#set
'''
s={1,1,2,2,3,3,4}
print(s)

output:
{1, 2, 3, 4}'

s={1,2}
print(type(s))

Output
<class 'set'>
'''
#functions

#add()=> add the values and string in set
'''
s1={1,2.3,4,5,6}
s1.add("krishna")
print(s1)

Output:
{1, 2.3, 'krishna', 4, 5, 6}
'''

#update=>add the list of values and sting in set
'''
s1={1,2.3,4,5,6}
s1.update([1,2.2,"krishna"])
print(s1)

Output:
{1, 2.3, 2.2, 4, 5, 6, 'krishna'}
'''
#remove=> remove value or sting in set
'''
s={1,1.2,"krishna",True}
s.remove(1.2)
print(s)

output:
{1, 'krishna'}
'''
#len()=> count the length of the set
'''
s={1,1.2,"krishna",True}
a=len(s)
print(a)

output:
3
'''
#funtions
#union=> print the combination of all values
'''
s1={1,2.2,3,4,}
s2={2,5,6,7,8,9,10}
a=s1.union(s2)
print(a)

output:

{1, 2.2, 3, 4, 2, 5, 6, 7, 8, 9, 10}
'''
#differance=> print the diff value in s1
'''
s1={1,2.2,3,4,5,6}
s2={2,5,6,7,8,9,10}
a=s1.difference(s2)
print(a)

output:
{1, 2.2, 3, 4}
'''
#intersection=>print the s1 and s2 commmen values
'''
s1={1,2.2,3,4,5,6}
s2={2,5,6,7,8,9,10}
a=s1.intersection(s2)
print(a)

output:
{5, 6}
'''
#issubset=>print the s1 and s2 both values are some print true or false
'''
s1={1,2.2,3,4,5,6}
s2={2,5,6,7,8,9,10}
a=s1.issubset(s2)
print(a)

output:
Flase
'''
#isdisjoint
'''
s1={1,2.2,3,4,5,6}
s2={2,5,6,7,8,9,10}
a=s1.isdisjoint(s2)
print(a)

output:
Flase
''' 