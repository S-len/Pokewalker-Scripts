import sys

def txt_to_bin(txt):
    data = txt.replace("\n", "")
    chunks = [data[i:i+8] for i in range(0, len(data), 8)]
    return bytearray([int(chunk,2) for chunk in chunks])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Correct syntax: img_to_txt.py in-file out-file")
        sys.exit()
        
    with open(sys.argv[1], "r") as in_file:
        with open(sys.argv[2], "wb") as out_file:
            out_file.write(txt_to_bin(in_file.read()))
