import sys

dir = "generic_number_csv/" # here we use classA;

input = dir + sys.argv[1]
output_file = sys.argv[2] + "_ortho.txt"
output = open(output_file,'w')

ortho_list = ['2x60','2x63','3x28','3x29','3x32','3x33','3x36','3x37','45x52','5x40','5x41','5x44','5x45','5x47','6x44','6x48','6x51','6x52','6x55','6x58','7x30','7x33','7x37','7x40','7x41']

with open(input, 'r') as f:
    for line in f:
        generic_number = line.split(",")[2]
        if generic_number in ortho_list:
            #print(line.split(",")[1])
            output.write(line.split(",")[1] + ",")

output.close()
    

