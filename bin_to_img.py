import sys
from PIL import Image
    
def bin_to_img(in_bin):
    inverted = bytes([b ^ 0b11111111 for b in in_bin])
    return Image.frombytes('1', (16, 768), inverted)
    
def unslice_image(in_img):
    if in_img == None:
        return in_img

    animated = True
    in_img = in_img.convert('L')

    lchunks = [in_img.crop((0,in_img.height-((i+1)*64),8,in_img.height-(i*64))) for i in range(0, 12 if animated else 6)]
    rchunks = [in_img.crop((8,in_img.height-((i+1)*64),16,in_img.height-(i*64))) for i in range(0, 12 if animated else 6)]
    
    out_img = Image.new('L', (48*2,64))

    for i in range(0,12 if animated else 6):
        out_img.paste(Image.blend(lchunks[i],rchunks[i],2/3), (i*8, 0))
    
    return out_img.transpose(Image.ROTATE_90)
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Correct syntax: bin_to_img.py in-file")
        sys.exit()
    with open(sys.argv[1], "rb") as in_bin:
        unslice_image(bin_to_img(in_bin.read())).show()