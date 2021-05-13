List1 = ['morning', 'afternoon', 'night']
List2 = ['Saturday', 'Sunday', 'Monday', 'Tuseday', 'Wednesday', 'Thursday', 'Friday']
List3 = []
for i in range(len(List2)) :
    for j in range(len(List1)) :
        x = str(List2[i]) + '-' + str(List1[j])
        List3.append(x)
print(List3)
