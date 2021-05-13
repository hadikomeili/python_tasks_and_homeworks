# home work , question 2

input_file = open('input-q-2.txt')
read_file = input_file.read()
# input_file.close()
chars = ['[', ']', '\n']
for ch in chars:
    read_file = read_file.replace(ch, ' ')

read_file_sentences = read_file.split('. ')
new_file = []
for s in read_file_sentences:
    s = s.lstrip().rstrip()
    if s.isnumeric():
        del s
    else:
        s = s + '.\n'
        new_file.append(s)

output_file_1 = open('output-q-2-1.txt', 'w')
output_file_1.writelines(new_file)
output_file_1.close()

#============================================== part 2

read_file_words = []
for sentences in read_file_sentences:
    words = sentences.split()
    for w in words:
        w = w.rstrip(',').rstrip(')').lstrip('(').rstrip('"').lstrip('"')
        if w not in read_file_words:
            read_file_words.append(w)

all_word_and_numbers = len(read_file_words)
cnt_numbers = 0
numbers = []
words = []
for x in read_file_words:
    if x.isnumeric():
        cnt_numbers += 1
        numbers.append(x)
    else:
        words.append(x)

# print(words)
# print(numbers)
number_of_words = len(words)
number_of_numbers = len(numbers)

output_file_2 = open('output-q-2-2.txt', 'w')
output_file_2.write(f'{words = }\n{number_of_words = }\n{numbers = }\n{number_of_numbers = }')
output_file_2.close()
 #========================================== part 3
upper_words = []
for w in words:
    if w.istitle() or w.isupper():
        upper_words.append(w)

# print(upper_words)
with open('output-q-2-3.txt', 'w') as output_file_3:
    print(*upper_words, sep=', ', file=output_file_3)

