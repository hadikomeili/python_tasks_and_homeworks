# Repetition of characters
s = input('enter info:')
chr_list = []
timesOfAppearance = []
for x in s :
    if x not in chr_list :
        chr_list.append(x)
        y = s.count(x)
        timesOfAppearance.append(y)
for i in range(len(chr_list)) :
    print(chr_list[i], ':', timesOfAppearance[i])
