Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d={'s1':10,"s2":20}
>>> d.get("s1")
10
>>> print(d.get("s3"))
None
>>> d.get("s3","simbu")
'simbu'
>>> print(d.get("s3"))
None
>>> print(d.get("s3"))
None
>>> d.get("s2","simbu")
20
>>> d
{'s1': 10, 's2': 20}
>>> help(d.get)
Help on built-in function get:

get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.

>>> d.items()
dict_items([('s1', 10), ('s2', 20)])
>>> d.keys()
dict_keys(['s1', 's2'])
>>> d.pop("s2")
20
>>> d
{'s1': 10}
>>> d.pop("s2")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.pop("s2")
KeyError: 's2'
>>> dd={"a1":10,"a2":20}
>>> dd
{'a1': 10, 'a2': 20}
>>> dd.pop("s3","key not found")
'key not found'
>>> dd
{'a1': 10, 'a2': 20}
>>> dd.popitem()
('a2', 20)
>>> dd
{'a1': 10}
>>> dd={"a1":10,"a2":20}
>>> dd
{'a1': 10, 'a2': 20}
>>> dd.pop()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dd.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> dd.setdefault('s1')
>>> dd
{'a1': 10, 'a2': 20, 's1': None}
>>> dd.setdefault('s1',30)
>>> dd
{'a1': 10, 'a2': 20, 's1': None}
>>> dd.setdefault('s2',30)
30
>>> dd
{'a1': 10, 'a2': 20, 's1': None, 's2': 30}
>>> dd.insert("s1",40)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dd.insert("s1",40)
AttributeError: 'dict' object has no attribute 'insert'
>>> dd.replace("s1",40)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dd.replace("s1",40)
AttributeError: 'dict' object has no attribute 'replace'
>>> dd
{'a1': 10, 'a2': 20, 's1': None, 's2': 30}
>>> d1={'a1':20,'a2':30}
>>> dd.update(d1)
>>> dd
{'a1': 20, 'a2': 30, 's1': None, 's2': 30}
>>> d2={'s1':50}
>>> dd.update(d2)
>>> dd
{'a1': 20, 'a2': 30, 's1': 50, 's2': 30}
>>> dd.values()
dict_values([20, 30, 50, 30])
>>> dir(dd)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
