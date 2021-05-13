# function for checking palindrome?
def revere_string(s) :
    p = s[::-1]
    return p
def is_palindrome(s) :
    if s == revere_string(s) :
        return True
    return False

s = input('Enter a string:\n')
x = is_palindrome(s)
print(x)

def be_palindrome(x: str):
    x = x.lower()
    return x == x[::-1]

x = input('enter string?')
print(be_palindrome(x))
