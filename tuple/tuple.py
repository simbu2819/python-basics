Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t(1,2,3)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    t(1,2,3)
NameError: name 't' is not defined
>>> t=(1,2,3)
>>> type(t)
<class 'tuple'>
>>> t[0]
1
>>> t[-2]
2
>>>  t[0]=10
SyntaxError: unexpected indent
>>> t[0]=10
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t[0]=10
TypeError: 'tuple' object does not support item assignment
>>> t[0]=tuple(10)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t[0]=tuple(10)
TypeError: 'int' object is not iterable
>>> t.count(2)
1
>>> t.count(10)
0
>>> 
