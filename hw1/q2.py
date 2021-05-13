# question 2
s = input('enter ur info:')
vowelsCnt = 0 
digitCnt = 0
sumOfDigits = 0
chrList = []
timesOfAppearance = []
for i in s :
    if i == 'a' or i == 'i' or i == 'o' or i == 'e' or i == 'u' :
        vowelsCnt += 1 
    x = str(i).isdigit()
    if x == True :
        digitCnt += 1 
        sumOfDigits = sumOfDigits + int(i)
    if i not in chrList :
        chrList.append(i)
        y = s.count(str(i))
        timesOfAppearance.append(y)
print('Vowels :', vowelsCnt)
print('Digits :', digitCnt)
print('Sum of digits : ', sumOfDigits)
for i in range(len(chrList)) :
    if timesOfAppearance[i] >= 2 and i < (len(chrList) - 1) :
        print('\'{}\':'.format(chrList[i]), timesOfAppearance[i], end=', ')
    elif timesOfAppearance[i] >= 2 and i == (len(chrList) - 1) :
        print('\'{}\':'.format(chrList[i]), timesOfAppearance[i])

