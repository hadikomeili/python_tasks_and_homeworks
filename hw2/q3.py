# find minimum of a good number with spesific divisors:

def divisors(n) :
    cnt = 0
    for i in range(1, n + 1) :
        if n % i == 0:
            cnt += 1
    return cnt

def good_number(n) :
    x = 0
    for i in range(1, n + 1) :
        x += i
    return x

k = int(input('enter k?'))
i = 0
while True :
    i = i + 1
    x = good_number(i)
    t = divisors(x)
    if k <= t :
        print(x)
        break
