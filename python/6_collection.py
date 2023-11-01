fruits = ["apple ","Orange","banana"]
x,y,z = fruits
print(x)
print(y)
print(z)

#lists 
 
print('\nlist modifications ::\n ')
list1 = [1,2,3,4,5]

print(list1)
print(list1[1: ]) #slicing list
print(list1[0])  #indexing
print(list1[-2]) #negative indexing

list1.reverse()   #reversing
print(list1)
list1.sort()     #sorting
print(list1) 
list1[0] = 'one ' #changing content 

#push/append 

list1.append('six')  #add an item to list 
print(list1)
list1.extend([10,11,12])  #add more items  to list 
print(list1) 

#pop

list1.pop(5)  #pop fifth element 
print(list1)

#nested list 

list2 = [1,2,[7,8,9],3,4,5]
print(list2)
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Dictionary  (imp = keys and curly braces )

marks = {'Anup':90 ,'Sanup':89,'panup':88}  #keys are anup sanup ...

print(marks['Anup']) #key is the index

marks['kanup'] = 88 #appending 
print(marks)

marks['kanup'] = 78 #editing
print(marks)
print(marks.keys())   #printing only keys
print(marks.items())   #printing items

#list in dictionary 
 
marks = {'Anup': [90,95,96] ,'Sanup':89,'panup':88}
print(marks)
print(marks['Anup'])
print(marks['Anup'][2]) 

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#tuples use small parenthesis ()
#items cant be changed in tuple

my_tuple = (20,23,56,87)
print(my_tuple)
print(my_tuple[-1]) #indexing, negatgive also works
print(my_tuple.index(56)) #finding the index of element 56 i.e. 2


#sets
