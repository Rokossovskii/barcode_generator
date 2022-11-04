from barcode_module import *
from drawing_barcode import drawing_barcode

def main():
    
    input_code = input("enter 12 number decimal code:\n")

    dec_barcode = calculate_last_number(input_code)

    write_encoding_data()
    bin_barcode = encoding_barecode(dec_barcode)

    print(dec_barcode)
    
    drawing_barcode(bin_barcode)

if(__name__ == '__main__'):
    main()

#772434561006