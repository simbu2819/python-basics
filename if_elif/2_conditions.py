# above 100 ur cheating
#80 100 a grade
#60 79 b grade
#40 59 c grade
#bellow 40 fail
student=input('enter marks')
student=int(student)

if student>100:
    print('u r cheating')

elif (student>=80 and student<=100) :
    print('a grade')
elif (student>=60 and student<=79) :
    print('b grade')
elif (student>=40 and student<=59) :
    print('c grade')
elif (student<40 and student>=0) :
    print('fail')
else:
    print('something is wrong may be b assignemt not sbited')
 
