# importing image object from PIL
import math
from PIL import Image, ImageDraw

def drawing_barcode(bin_barcode):
    width, height = 440, 300
    barcode = Image.new("RGB", (width, width),color="white")

    for x,bin_num in enumerate(bin_barcode):
        shape = [(40+x*2, 40), (40+x*2, width - 40)]
        img1 = ImageDraw.Draw(barcode)
        if(bin_num == '1'):
            img1.line(shape, "black", width = 2)
        else:
            img1.line(shape, "white", width = 2)

        
        

    barcode.show()
