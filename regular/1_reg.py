import re

mobiles=['1234567890','12124344353','12388373378379','9881238964','7208812345',
         '6367637261','77777777712','43748744123','54546561234','666666666612345',
         '1 12 123 1234 12345a','a1111111']

'''
mathods
#search('pattern','string_data')
#match('pattern','string_data')
#findall('pattern','string_data')
'''

#print(re.search('..','mobiles'))
#print(re.findall('..',data))
#print(re.match('sila',data))



for item in mobiles:
    if re.search('^[^9876]\d{9}$',item):
        print(item)
"""
^ starts with
$ ends with
. means any single character
{number}
\d means only 
* means zero or more
+ means one or more
