import PIL
from PIL import Image
import sys
 
def img_to_txt(in_img):
    img = in_img.convert('1')
    return "".join([str(int(img.getpixel((x,y)) == 0)) for y in range(0,img.height) for x in range(0,img.width)])
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Correct syntax: img_to_txt.py in-file [out-file]")
        sys.exit()
        
    with Image.open(sys.argv[1]) as in_img:
        data = img_to_txt(in_img)
        
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as out_file:
            out_file.write(data)
    else:
        print(data)    
