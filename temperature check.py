print('\nPlease enter your name ..............\n')
a=input()
print(a.capitalize()+',please enter your current temperature')
g=input()
r=int(g)
if r>=30 :
    print('It is hot!' )    
elif 15<=r<=29:
     print('It is warm')   
else:
    print('It is cold')   