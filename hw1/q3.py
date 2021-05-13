# take n marks and get out Maximum, Minimum an Average.(with Functions)
marks = map(int, input('Enter ur marks:').split())
marks = list(marks)
print('Maximum:', max(marks))
print('Minimum:', min(marks))
print('Average:', sum(marks)/len(marks))

# take n marks and get out Maximum, Minimum an Average.(without Functions)
marks2 = input('Enter ur marks:').split()
n = numberOfmarks = len(marks2)
orderedMarks2 = [0] * n
sumOfMarks = 0
for i in range(n) :
    orderedMarks2[i] = int(marks2[i])
    sumOfMarks = sumOfMarks + orderedMarks2[i]
for i in range(n) :
    max_index = i
    for j in range(i, n) :
        if orderedMarks2[max_index] < orderedMarks2[j] :
            max_index = j
        orderedMarks2[i], orderedMarks2[max_index] = orderedMarks2[max_index], orderedMarks2[i]
print('Maximum:', orderedMarks2[0])
print('Minimum:', orderedMarks2[-1])
print('Average:', sumOfMarks/len(marks2))

