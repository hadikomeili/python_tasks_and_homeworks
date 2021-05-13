# sange pa business !!!
def is_prime(n):
    i = 0
    for i in range(n-1,0,-1):
        if n % i == 0:
            break
    if i == 1:
        return True
    return False


def prime_counter(n):
    cnt = 0
    for j in range(n):
        if is_prime(j) == True:
            cnt += 1
    return cnt


def prime_divisors(n):
    cnt = 0
    for i in range(1,n):
        if n % i == 0:
            if is_prime(i) == True:
                cnt += 1
    return cnt


n = int(input())
weights = [0]*n
price = 0
for j in range(n):
    weights[j] = int(input())
for k in range(n):
    if is_prime(weights[k]) == True:
        price += prime_counter(weights[k])
    else:
        price += prime_divisors(weights[k])
if is_prime(price) == True:
    price -= prime_counter(price)
else:
    price -= prime_divisors(price)
print(price)
