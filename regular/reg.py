Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.search('a*','aaaaabbbbbaaaa')
<re.Match object; span=(0, 5), match='aaaaa'>
>>> re.search('b*','aaaaabbbbbaaaa')
<re.Match object; span=(0, 0), match=''>
>>> re.search('a+','aaabbbaaa')
<re.Match object; span=(0, 3), match='aaa'>
>>> re.search('a+','bbbaaa')
<re.Match object; span=(3, 6), match='aaa'>
>>> 
