# A - 0 B - 1 C - 2
from tokenize import String

barcode_encoding_dic = {
    'A':[],
    'B':[],
    'C':[]
}
encoding_table = []

middle_guard = '01010'
outside_boundieries_guard = '101'

def write_encoding_data():
    with open('./barcode/barcode_encoding_data.txt') as file:
        for line in file:
            line = line.split(' ')
            barcode_encoding_dic.get('A').append(line[1])
            barcode_encoding_dic.get('B').append(line[2])
            barcode_encoding_dic.get('C').append(line[3])

    with open('./barcode/barcode_how_to_encode_data.txt') as file:
        for line in file:
            line = line.strip('\n').split('\t')
            encoding_table.append(line)
    
def calculate_last_number(input_string:str) -> str:
    sum = 0

    if(len(input_string)>12):
        input_string = input_string[:12]
    else:
        while(len(input_string)<12):
            input_string = '0' + input_string

    try:
        for index,char in enumerate(input_string):
            if(index%2 == 0):
                sum += int(char) * 3
            else:
                sum += int(char)
    except:
        print('not all deimal')
        return
    sum = 10 - (sum%10)
    if(sum == 10): sum = 0

    return str(sum) + input_string 

def encoding_barecode(input_string:str) -> str:
    first_num = int(input_string[0])
    ouptut_code = outside_boundieries_guard
    for index,(num,key) in enumerate(zip(input_string[1:],encoding_table[first_num])):
        if(index == 6): 
            ouptut_code += middle_guard
        ouptut_code += barcode_encoding_dic.get(key)[int(num)]
    ouptut_code += outside_boundieries_guard
    return ouptut_code