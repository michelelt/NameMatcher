def compact_names(name):
    letters = []
    for letter in name:
        if letter not in letters:
            letters.append(letter)
    return letters

def count_occs(name, letters):
    occs=[]
    for letter in letters:

        occs.append(str(name.count(letter)))
    return occs

def print_name_occs(letters, occs):
    num_lines = int(max(occs))
    for line in range(0,num_lines):
        my_str = ''
        for i, let in enumerate(letters):
            if int(occs[i]) > line: my_str += let+ ' '
            else: my_str+= '  '
        print(my_str)


def compute_new_occs(occs):
    head=0
    tail=len(occs)-1
    new_occs = []
    if len(occs) %2 == 0:
        while head <= tail:
            sum = int(occs[head]) + int(occs[tail])
            sum = str(sum)
            for digit in sum:
                new_occs.append(digit)
            head+=1
            tail-=1
    else:
        while head != tail:
            sum = int(occs[head]) + int(occs[tail])
            sum = str(sum)
            for digit in sum:
                new_occs.append(digit)
            head+=1
            tail-=1
        new_occs.append(occs[tail])
    return new_occs

def custom_print(array):
    my_str = ' '.join(array)
    print(my_str)
