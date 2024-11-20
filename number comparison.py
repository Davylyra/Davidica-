print('\nPlease enter your name ..............\n')
a=input()
print(a.capitalize()+',please enter your first number\n')
g=input()
r=int(g)
print(a.capitalize()+',please enter your second number\n')
e=input()
s=int(e)
if r>s:
    print('The first number is greater')
if r<s:
    print('The second number is greater')        
if r==s:
    print('Both are equal')