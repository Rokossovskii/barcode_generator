from PIL import Image, ImageDraw

def drawing_barcode(bin_barcode):
    b_width = 4
    width, height = b_width*95+80, 300
    barcode = Image.new("RGB", (width, width),color="white")

    for x,bin_num in enumerate(bin_barcode):
        shape = [(40+x*b_width, 40), (40+x*b_width, width - 40)]
        line = ImageDraw.Draw(barcode)
        if(bin_num == '1'):
            line.line(shape, "black", width = b_width)
        else:
            line.line(shape, "white", width = b_width)
        
    barcode.save("barcode.png")

