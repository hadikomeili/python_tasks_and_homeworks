# simple calculator (numbers and operator splited with whithspace)
a, b, c = input('Enter your operation:').split()
if b == '+' :
    result = int(a) + int(c)
elif b == '-' :
    result = int(a) - int(c)
elif b == '*' :
    result = int(a) * int(c)
else :
    result = int(a) / int(c)
print('Result =', result)

# simple calculator (numbers and operator splited without whithspace)
s = input('enter ur operation?')
if '+' in s :
    a, c = s.split('+')
    result = int(a) + int(c)
elif '-' in s :
    a, c = s.split('-')
    result = int(a) - int(c)
elif '*' in s :
    a, c = s.split('*')
    result = int(a) * int(c)
else :
    a, c = s.split('/')
    result = int(a) / int(c)
print('Result =', result)


