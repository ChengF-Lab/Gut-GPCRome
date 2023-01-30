from sys import breakpointhook
import sys
import re

dir = "docking_results/"

input = dir + sys.argv[1]

file1 = "results_resi5.txt"

list1 = []

    
with open (input, "r") as g:
    for line in g:
        po_name = line.split(" ")[:-1]
        list1.append(po_name)



with open (file1, "r") as f:
    for line in f:
        all_name = line.split(" ")[:-1]
        if all_name in list1:
            print(line, end="")

