import ndspy.narc
import ndspy.lz10
from bin_to_img import *

def dump(path):
    narc = ndspy.narc.NARC.fromFile(path)
    data = ndspy.lz10.decompress(narc.files[0])

    for id in range(0, len(narc.files)):
        unslice_image(bin_to_img(ndspy.lz10.decompress(narc.files[id]))).save("./out/"+str(id)+".png", "PNG")
        print(str(id)+": done.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Correct syntax: sprite_dump.py in-file")
        sys.exit()
    dump(sys.argv[1])