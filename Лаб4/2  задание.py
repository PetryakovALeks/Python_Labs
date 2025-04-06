input_file = open('input_floats.txt', 'r')

numbers = [float(num) for num in input_file.read().split()]

input_file.close()

lengths = []

current_len = 1
is_up = None
is_down = None
for i in range(1, len(numbers)):
    
    if numbers[i] > numbers[i - 1]:
        if is_down:
            lengths.append(current_len)
            current_len = 1
            is_down = False
        is_up = True
        current_len += 1
    elif numbers[i] < numbers[i - 1]:
        if is_up:
            
            lengths.append(current_len)
            current_len = 1
            is_up = False
        is_down = True
        current_len += 1
    else:
        
        lengths.append(current_len)
        current_len = 1
        is_up = None
        is_down = None


lengths.append(current_len)


output_file = open('output_lengths.txt', 'w')


output_file.write(' '.join(map(str, lengths)))


output_file.close()