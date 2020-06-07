Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=lambda x,y:x+y
>>> x=5
>>> y=6
>>> a=lambda x,y:x+y
>>> a
<function <lambda> at 0x0113B588>
>>> a(1,2)
3
>>> a=lambda x,y: x+y;print("hi")
hi
>>> a(10,20)
30
>>> a=lambda x,y: x+y:print("hi")
SyntaxError: invalid syntax
>>> a=lambda x,y: x+y
>>> a(5,5)
10
>>> a=lambda x,y: x+y :(print("hi"))
SyntaxError: invalid syntax
>>> a=lambda x,y:(x+y,print("hi"))
>>> a(10,5)
hi
(15, None)
>>> a=lambda x,y:(x+y,x-y,x*y)
>>> a(10,20)
(30, -10, 200)
>>> a=lambda x,y:print(x+y,x-y,x*y)
>>> a(10,20)
30 -10 200
>>> a=lambda x,y:print("\n",x+y,"\n",x-y,"\n",x*y)
>>> a(10,20)

 30 
 -10 
 200
>>> l=[[1,2,3],[5,1,6],[3,3,2]]
>>> l1=[[1,2,3],[2,1,4],[3,3,10]]
>>> l1.sort(key=lambda x:x[1])
>>> l1
[[2, 1, 4], [1, 2, 3], [3, 3, 10]]
>>> l1.sort(key=lambda x:x[1],reverse=True)
>>> l1
[[3, 3, 10], [1, 2, 3], [2, 1, 4]]
>>> l2=[10,20,30,50]
>>> l3=[15,25,35,45]
>>> l2.update(l3)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l2.update(l3)
AttributeError: 'list' object has no attribute 'update'
>>> a=map(lambda x:x+5,l)
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list(a)
  File "<pyshell#29>", line 1, in <lambda>
    a=map(lambda x:x+5,l)
TypeError: can only concatenate list (not "int") to list
>>> l
[[1, 2, 3], [5, 1, 6], [3, 3, 2]]
>>> a=map(lambda x:x+5,l1)
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list(a)
  File "<pyshell#32>", line 1, in <lambda>
    a=map(lambda x:x+5,l1)
TypeError: can only concatenate list (not "int") to list
>>> a=map(lambda x:x+5,l2)
>>> list(a)
[15, 25, 35, 55]
>>> l2=map(lambda x:x+5,l)
>>> l2
<map object at 0x036B51B0>
>>> k=list(l2)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    k=list(l2)
  File "<pyshell#36>", line 1, in <lambda>
    l2=map(lambda x:x+5,l)
TypeError: can only concatenate list (not "int") to list
>>> l2
<map object at 0x036B51B0>
>>> list(l2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(l2)
  File "<pyshell#36>", line 1, in <lambda>
    l2=map(lambda x:x+5,l)
TypeError: can only concatenate list (not "int") to list
>>> l2=map(lambda x:x[1]+5,l)
>>> list(l2)
[7, 6, 8]
>>> l=[1,2,10,30,1,2,40,60,80,95,3]
>>> a=map(lambda x:x>35,l)
>>> list(a)
[False, False, False, False, False, False, True, True, True, True, False]
>>> a=map(lambda x:print(x>35),x),l)
SyntaxError: invalid syntax
>>> a=map(lambda x:print((x>35)),l)
>>> print(a)
<map object at 0x036B5710>
>>> print(list(a))
False
False
False
False
False
False
True
True
True
True
False
[None, None, None, None, None, None, None, None, None, None, None]
>>> a=map(lambda x:print((x>35),x),l)
>>> list(a)
False 1
False 2
False 10
False 30
False 1
False 2
True 40
True 60
True 80
True 95
False 3
[None, None, None, None, None, None, None, None, None, None, None]
>>> print(x)
5
>>> a=map(lambda x:(x>=35) && (x<=60)),l)
SyntaxError: invalid syntax
>>> a=map(lambda x:(x>=35) and (x<=60)),l)
SyntaxError: invalid syntax
>>> a=map(lambda x:(x>=35) and (x<=60),l)
>>> list(a)
[False, False, False, False, False, False, True, True, False, False, False]
>>> a=map(lambda x:(x>=35) and (x<=60) print(x),l)
SyntaxError: invalid syntax
>>> a=map(lambda x:(x>=35) and (x<=60), print(x),l)
5
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a=map(lambda x:(x>=35) and (x<=60), print(x),l)
TypeError: 'NoneType' object is not iterable
>>> a=map(lambda x:(x>=35) and (x<=60),l)
>>> d=[1,2,0,10,30]
>>> c=filter(None,d)
>>> list(c)
[1, 2, 10, 30]
>>> bool(10)
True
>>> e=filter(d)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    e=filter(d)
TypeError: filter expected 2 arguments, got 1
>>> e=filter("hi",d)
>>> list(e)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list(e)
TypeError: 'str' object is not callable
>>> e=filter(del,d)
SyntaxError: invalid syntax
>>> k=filter(None,a)
>>> k
<filter object at 0x036DDF70>
>>> list(k)
[True, True]
>>> l
[1, 2, 10, 30, 1, 2, 40, 60, 80, 95, 3]
>>> a=map(lambda x:filter(None,x>=35), print(x),l)
5
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a=map(lambda x:filter(None,x>=35), print(x),l)
TypeError: 'NoneType' object is not iterable
>>> a=map(lambda x:filter(x>=35), print(x),l)
5
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a=map(lambda x:filter(x>=35), print(x),l)
TypeError: 'NoneType' object is not iterable
>>> k=filter(lambda x:x>=40 and x<=80,l)
>>> list(k)
[40, 60, 80]
>>> 
