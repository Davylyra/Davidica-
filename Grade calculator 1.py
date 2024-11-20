print('\nPlease enter your name ..............\n')
a=input()
print(a.capitalize()+',please enter your score (0-100) to see your grade')
s=input()
z=int(s)
if z>=90:
    print('Grade A')
if 80<=z<=89 :    
     print('Grade B ')
if 70<= z<=79:
     print('Grade C ')
if 60<=z<=69:     
          print('Grade  D')
if z<60:
           print('Grade F ')
          
