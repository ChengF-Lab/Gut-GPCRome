from sys import breakpointhook
import sys
import re
# python pocket_generic_numer_match.py pocket_ClassA.txt pocket_ClassA_name_brief.txt pocket_ClassA_name.txt

dir = "pockets/"
dir2 = ""

input = dir + sys.argv[1]  #pocket_ClassA.txt

ref = sys.argv[2]  # pocket_ClassA_name_brief.txt
ref2 = dir2 + ref + "_ortho.txt"

# obtain residue numbers of pocket that match generic number
with open(ref2, "r") as f:
    S = f.read().split(",")

P = list(i for i in S)
P.pop()

#obtain residue number of identified pocket
T = []
with open(input, 'r') as f:
    for line in f:
        if "ATOM" in line:
            po_number = line.split()[5]
            T.append(po_number)


intersection = list(set(P) & set(T))

if (len(intersection)) >=5:
    print(sys.argv[3] + "," + "1")

else:
    print(sys.argv[3] + "," + "0")

