import cv2
import numpy


def to_binary(obj):
    if type(obj) == str:
        return ''.join([format(ord(i), "08b") for i in obj])
    elif type(obj) == bytes or type(obj) == numpy.ndarray:
        return [format(i, "08b") for i in obj]


def decrypt(image):
    bin_msg = ""

    for i in image:
        for j in i:
            r, g, b = to_binary(j)
            bin_msg += r[-1]
            bin_msg += g[-1]
            bin_msg += b[-1]

    byte_array = [bin_msg[i: i+8] for i in range(0, len(bin_msg), 8)]

    decrypted_msg = ""
    for byte in byte_array:
        decrypted_msg += chr(int(byte, 2))
        if(decrypted_msg[-6:] == "$$$$$$"):
            break

    return decrypted_msg[:-6]


def main():
    img_name = input("Enter the name of image to be decrypted : ")
    im = cv2.imread(img_name)

    msg = decrypt(im)

    print(msg)


if __name__ == "__main__":
    main()
