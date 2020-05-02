import sys

from functions import *

if __name__=='__main__':
    if len(sys.argv) == 1:
        name1 = 'michelecocca'
        name2 = 'michelecocca'
    else:
        name1 = sys.argv[1]
        name2 = sys.argv[2]

    letters = compact_names(name1+name2)
    occs = count_occs(name1+name2, letters)
    print_name_occs(letters, occs)

    while True:
        custom_print(occs)
        if len(occs) == 2: break
        occs = compute_new_occs(occs)

