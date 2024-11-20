print('\nPlease enter your name ..............\n')
a=input()
print(a.capitalize()+',please enter your age .............\n')
b=input()
c=int(b)
if c > 18 :
    print(a.capitalize()+',you are an adult')
else:
    print(a.capitalize()+', you are a minor')   