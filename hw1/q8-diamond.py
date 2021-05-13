# print a triangle with * based on 'n' :

n = int(input('enter a number:'))
if (n % 2) == 0 :
    n = n-1
    print(f'we print diamond for {n} ')
for i in range(1, n+1, 2) :
    x = '*'*i
    print(x.center(n))
for j in range((n-2), 0, -2) :
    y = '*'*j
    print(y.center(n))


