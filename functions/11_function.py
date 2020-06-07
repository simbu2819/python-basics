#functions
#3 types

"""
1.pre-defined function
 print(),input(),range(),len(),min(),max(),etc...

2.user-defined function
  def function_name() 
3.anonymus function(lamda)
"""




"""
def myaddition(a,b):
    print(a)
    print(b)
    print('addition = ',a+b)
    return 1,2
#print(myaddition(10,20))
c=myaddition(10,20)
print(c)    
print(type(c))
"""


"""
 based on reuired arguments functions are

     1. requiired argument functions
     2. keyword argument functions
     3. default argument functions
     4.variable length argument functions
    """

#required argument
"""
def add(a,b):
    print(a)
    print(b)
    print(a+b)
add(b=20,a=10)
"""
#default argument
"""def add(a,b=0):
    print(a)
    print(b)
    print(a+b)

add(1)
"""
#variable length argument
def add(a,b,*simbu):
    print(a)
    print(b)
    print(sum(simbu))

add(1,2,4,5)
