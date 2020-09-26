import PIL
from PIL import Image
from txt_to_bin import *
from img_to_txt import *
from slice_image import *

def img_to_bin(in_file):
    return txt_to_bin(img_to_txt(slice_image(in_file)))
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Correct syntax: img_to_bin.py in-file out-file")
        sys.exit()
        
    with Image.open(sys.argv[1]) as in_file:
        with open(sys.argv[2], "wb") as out_file:
            out_file.write(img_to_bin(in_file))