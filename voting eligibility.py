print('\nPlease enter your name ..............\n')
a=input()
print(a.capitalize()+',please enter the name of your country\n')
g=input()
print(a.capitalize()+',please enter your age\n')
e=input()
s=int(e)
if s>=18 and g=='ghana':
    print('You can vote')
else:
    print('You cannot vote')    
 

