#string


s='krishna'
s1="this is siva prasad"
s2='''
 this 
is 
string'''

#functions
#upper=> conver all lower case to upper case letters
'''
a=s2.upper()
print(a)

out put

THIS  
IS    
STRING
'''
#lower =>convert all upper case to lower case letters
'''
a="Krishna"
print(a.lower())

output 

krishna'''

#replace =>replace the words
'''
a=s2.replace('is','are')
print(a)

output= 

thare 
are   
string'''

#split => saparation of srting 
'''
a=s1.split()
print(a)

output=
['this', 'is', 'siva', 'prasad']'''

#strip=> elemate the spces
'''
a=s2.strip()
print(a)

Output=
this 
is   
string
'''
#startwith =>> stating letter correct or not
'''
a= s.startswith('k')
print(a)

Output

true '''

#endswith => ending letter correct or not
'''
a=s.endswith('a')
print(a)

output 

true'''

#format=> add the string using format
'''
print("this is a {}".format("test"))

Output
 this is a test
 '''

#count => count the no.of commen strings
'''
a=s1.count('is')
print(a)

output 
is = 2'''

#length=> calculate no.of character(length) in stings
'''
a=len(s)
print(a)

Output

len=7'''