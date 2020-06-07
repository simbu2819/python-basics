Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="good marning"
>>> s
'good marning'
>>> s[0:5:2]
'go '
>>> s[0:3:2]
'go'
>>> s[13]=10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[13]=10
TypeError: 'str' object does not support item assignment
>>> s1=s
>>> s1
'good marning'
>>> s="good"
>>> s
'good'
>>> id(s1)
59522048
>>> id(s)
59855296
>>> print(s[1:5]+"simbu")
oodsimbu
>>> s
'good'
>>> del(s1)
>>> s1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s1
NameError: name 's1' is not defined
>>> id(s1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    id(s1)
NameError: name 's1' is not defined
>>> len(s)
4
>>> s.upper()
'GOOD'
>>> s.lower()
'good'
>>> s.upper()
'GOOD'
>>> s.casefold()
'good'
>>> s.replace("good","great")
'great'
>>> s1="good morning"
>>> s.replace("good","greate").replace("morning","perform")
'greate'
>>> s1
'good morning'
>>> s1.replace("good","greate").replace("morning","perform")
'greate perform'
>>> s1
'good morning'
>>> s1.split("a",2)
['good morning']
>>> s1.split("g",2)
['', 'ood mornin', '']
>>> s1
'good morning'
>>> s1.capitalize()
'Good morning'
>>> s1.title()
'Good Morning'
>>> s1.find("d")
3
>>> s1.find("d",5)
-1
>>> s1
'good morning'
>>> len(s1)
12
>>> s1.center(15,"@")
'@@good morning@'
>>> s1.center(14,"@")
'@good morning@'
>>> s1.center(20,"@")
'@@@@good morning@@@@'
>>> s1.center(19,"@")
'@@@@good morning@@@'
>>> s1.find("0",5)
-1
>>> s1
'good morning'
>>> s1.find("o",5)
6
>>> s
'good'
>>> s1
'good morning'
>>> s1.center(19,"")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s1.center(19,"")
TypeError: The fill character must be exactly one character long
>>> s1.center(19," ")
'    good morning   '
>>> s1.lstrip()
'good morning'
>>> s1.center(20," ")
'    good morning    '
>>> s1.lstrip()
'good morning'
>>> s1
'good morning'
>>> s1='   hi   '
>>> s1
'   hi   '
>>> s1.lstrip()
'hi   '
>>> s1="good morning"
>>> s1.index("m")
5
>>> s1.index("g")
0
>>> min(s1)
' '
>>> max(s1)
'r'
>>> s1
'good morning'
>>> max(s1)
'r'
>>> s1(::-1)
SyntaxError: invalid syntax
>>> s1[::-1]
'gninrom doog'
>>> print("hello {} {} ".format("simbu","good morning"))
hello simbu good morning 
>>> print("hello {1} {1} ".format("simbu","good morning"))
hello good morning good morning 
>>> print("hello {1} {0} ".format("simbu","good morning"))
hello good morning simbu 
>>> print("hello {gret} {name} ".format(name="simbu",gret="good morning"))
hello good morning simbu 
>>> 
============= RESTART: C:/Users/exam/Desktop/16f61f0035/task4.py =============
enter name:simbu
enter greatings :hi
Traceback (most recent call last):
  File "C:/Users/exam/Desktop/16f61f0035/task4.py", line 3, in <module>
    print("hello {name} {gret}".format(name,gret))
KeyError: 'name'
>>> 
============= RESTART: C:/Users/exam/Desktop/16f61f0035/task4.py =============
enter name:simbu
enter greatings :hi
hello simbu hi
>>> lang=["c","java","webapplication","python","ai"]
>>> a[1,"string",[1,2,3],15.5,True]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a[1,"string",[1,2,3],15.5,True]
NameError: name 'a' is not defined
>>> a=[1,"string",[1,2,3],15.5,True]
>>> a
[1, 'string', [1, 2, 3], 15.5, True]
>>> lang[0]="c++"
>>> lang
['c++', 'java', 'webapplication', 'python', 'ai']
>>> lang*3
['c++', 'java', 'webapplication', 'python', 'ai', 'c++', 'java', 'webapplication', 'python', 'ai', 'c++', 'java', 'webapplication', 'python', 'ai']
>>> lang1=["ql"]
>>> lang+lang1
['c++', 'java', 'webapplication', 'python', 'ai', 'ql']
>>> lang1=["sql"]
>>> lang+lang1
['c++', 'java', 'webapplication', 'python', 'ai', 'sql']
>>> lang.append(".net")
>>> lang
['c++', 'java', 'webapplication', 'python', 'ai', '.net']
>>> lang.append(["sql","mysql"])
>>> lang
['c++', 'java', 'webapplication', 'python', 'ai', '.net', ['sql', 'mysql']]
>>> lang[7][0]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    lang[7][0]
IndexError: list index out of range
>>> lang[6][0]
'sql'
>>> lang[6].append("no  sql")
>>> lang[6]
['sql', 'mysql', 'no  sql']
>>> lang.insert(0,"work")

>>> lang
['work', 'c++', 'java', 'webapplication', 'python', 'ai', '.net', ['sql', 'mysql', 'no  sql']]
>>> lang.insert(10,"work")
>>> lang
['work', 'c++', 'java', 'webapplication', 'python', 'ai', '.net', ['sql', 'mysql', 'no  sql'], 'work']
>>> lang.insert([6][0],"work")
>>> lang
['work', 'c++', 'java', 'webapplication', 'python', 'ai', 'work', '.net', ['sql', 'mysql', 'no  sql'], 'work']
>>> lang.insert([7][0],"work")
>>> lang
['work', 'c++', 'java', 'webapplication', 'python', 'ai', 'work', 'work', '.net', ['sql', 'mysql', 'no  sql'], 'work']
>>> lang[7].insert(0,"work")
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    lang[7].insert(0,"work")
AttributeError: 'str' object has no attribute 'insert'
>>> lang.insert([8]0,"work")
SyntaxError: invalid syntax
>>> lang[9].insert(0,"work")
>>> lang
['work', 'c++', 'java', 'webapplication', 'python', 'ai', 'work', 'work', '.net', ['work', 'sql', 'mysql', 'no  sql'], 'work']
>>> lang1
['sql']
>>> l1=[1,2,3,4,5]
>>> l=l1
>>> l.clear()
>>> l1
[]
>>> id(l)
9808792
>>> id(l1)
9808792
>>> lang1=lang.copy()
>>> lang1
['work', 'c++', 'java', 'webapplication', 'python', 'ai', 'work', 'work', '.net', ['work', 'sql', 'mysql', 'no  sql'], 'work']
>>> lang.clear()
>>> lang
[]
>>> lang1
['work', 'c++', 'java', 'webapplication', 'python', 'ai', 'work', 'work', '.net', ['work', 'sql', 'mysql', 'no  sql'], 'work']
>>> lang1.pop()
'work'
>>> lang1
['work', 'c++', 'java', 'webapplication', 'python', 'ai', 'work', 'work', '.net', ['work', 'sql', 'mysql', 'no  sql']]
>>> lang.push("simbu")
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    lang.push("simbu")
AttributeError: 'list' object has no attribute 'push'
>>> lang.push(["simbu"])
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    lang.push(["simbu"])
AttributeError: 'list' object has no attribute 'push'
>>> 
