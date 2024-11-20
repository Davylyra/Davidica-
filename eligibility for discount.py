print('\nPlease enter your name ..............\n')
a=input()
print(a.capitalize()+',please enter your age\n')
g=input()
r=int(g)
if r <12 or r > 65:
    print('You are eligible for a discount')
else:
    print('No discount aavailable')    