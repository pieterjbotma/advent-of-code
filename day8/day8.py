# digits_list = [[set(digit) for digit in line.split(' | ')[1].split()] for line in open('day8-example.txt')]
# unique_list = [[set(digit) for digit in line.split(' | ')[0].split()] for line in open('day8-example.txt')]

# digit_counts = [[len(digit) for list in digits_list for digit in list].count(i) for i in range(0,8)]
# print(sum(digit_counts[i] for i in [2,3,4,7]))

def extract_digit(line: str):

    unique_str, digits_str = line.split(' | ')
    unique_list = [set(digit) for digit in unique_str.split()]
    digits_list = [set(digit) for digit in digits_str.split()]
        
    segment_len = [len(digit) for digit in unique_list]
    s1 = unique_list[segment_len.index(2)]
    s4 = unique_list[segment_len.index(4)]
    s7 = unique_list[segment_len.index(3)]
    s8 = unique_list[segment_len.index(7)]

    segment_sums = ([sum(1 for digit in unique_list if c in digit) for c in 'abcdefg'])
    f = set('abcdefg'[segment_sums.index(9)])
    e = set('abcdefg'[segment_sums.index(4)])
    b = set('abcdefg'[segment_sums.index(6)])
    a = s1^s7
    c = s1-f
    d = s4-b-c-f
    g = s8-a-b-c-d-e-f

    truth = [
        a|b|c|e|f|g,
        c|f,
        a|c|d|e|g,
        a|c|d|f|g,
        b|c|d|f,
        a|b|d|f|g,
        a|b|d|e|f|g,
        a|c|f,
        a|b|c|d|e|f|g,
        a|b|c|d|f|g
    ]

    return int(''.join(map(str,[truth.index(digit) for digit in digits_list])))

with open('day8-input.txt') as f:
    print(sum(extract_digit(line) for line in f))


