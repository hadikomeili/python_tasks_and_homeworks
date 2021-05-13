
num_dict = {
    'one' : 1, 'two' : 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
    'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20

}

input_file = open('input-q-1.txt')
read_file = input_file.read()

for x in read_file.split():
    if x.lower() in num_dict.keys():
        read_file = read_file.replace(str(x.lower()), str(num_dict[x]))

output_file = open('output-q-1.txt', 'w')
output_file.write(read_file)
