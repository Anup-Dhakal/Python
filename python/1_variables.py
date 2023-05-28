
#no need to indicate data types no need of colon ; 
#variable are case insensitive a and A are different 
#variable name should not start with number 

#Examples
a = 10              #integer
b = 10.5            #float
c = 'Z'             #character 
d = "Happy coding"   #string  *****IMP single quotes can also be used 

print(a)
print(b)
print(c)
print(d)

#casting 

x= int(10)
y = float(10)
z =str(10) #10 used and string 
xy = str("I'm Coder ")

print(x)
print(y)
print(z)
print(xy)

#getting type
print(type(x))
print(type(y))
print(type(z))
print(type(xy))

#many to many and one to many

xa=ya=za = 10 #one to many 
print (xa)
print(ya)
print (za)
 
x1,y1,z1 = "anup" , "dhakal", "Tansen"
print(x1)
print(y1)
print(z1)

 
#Global Variable

#variable outside function 
#can be used global keyboard before variable (not mandatory)

def sum(a,b):    ##########<<<<<<colon 
    print(a+b)
    print (x) #x used as global variable

sum(20,30)

