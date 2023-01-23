
#list
"""a=[1,2.5,"siva",True]
print(a)
print(type(a))

out=[1,2.5,"siva",True]
<class 'list'>
"""


#list methods(funtions)
#append=> add the value in end of the list
'''a=[1,2.5,"siva",True]
a.append(200)
print(a)
print(type(a))

out =a=[1,2.5,"siva",True,200]
<class 'list'>'''

#extend=> add the list in list

'''a=[1,2.5,"siva",True]
a.extend([[1,4.0,"krishna",False]])
print(a)
print(type(a))

out = [1, 2.5, 'siva', True, [1, 4.0, 'krishna', False]]
<class 'list'>'''

#index=> print the the index
'''
a=[1, 2.5, 'siva', True, [1, 4.0, 'krishna', False]]
print(a[4][1])

out = 4.0'''

#insert=> add the value in list particuler position
'''
a=[1,2.5,"siva",True]
a.insert(1,1)
print(a)
print(type(a))

out =[1, 1, 2.5, 'siva', True]
<class 'list'>'''

#pop => delete the value in list 
'''
a=[1,1,2.5,"siva",True]
a.pop(1)
print(a)
print(type(a))

out = [1, 2.5, 'siva', True]
      <class 'list'>'''

#count => calculate the repeted values in the list
''''
a=[1,1,2.5,"siva",True] # true = 1, flase =0
print(a.count(1))

out = 3'''
'''
a=[1,1,2.5,"siva",False,2.5] # true = 1, flase =0
print(a.count(1))
print(a.count(2.5))

out = 1=2 time
      2.5=2 time'''

#lengtt(len) => count the length of list
'''
a=[1,1,2.5,"siva",False,2.5] 
print(len(a))

out = 6 '''

#sort => convert the list in assending order
'''
a=[1,1,2.5,100,10,15,50,20,11,17]
a.sort()
print(a)

Output =[1, 1, 2.5, 10, 11, 15, 17, 20, 50, 100]'''

#reverse => print the list in reverse order

'''
a=[1,1,2.5,"siva",True]
a.reverse()
print(a)

out= [True, 'siva', 2.5, 1, 1]'''