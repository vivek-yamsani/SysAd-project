import cv2
import numpy


def to_binary(obj):
    if type(obj) == str:
        return ''.join([format(ord(i), "08b") for i in obj])
    elif type(obj) == bytes or type(obj) == numpy.ndarray:
        return [format(i, "08b") for i in obj]


def hide_msg(image, msg):
    msg += "$$$$$$"
    idx = 0
    bin_msg = to_binary(msg)
    bin_len = len(bin_msg)

    for i in image:
        for j in i:
            r, g, b = to_binary(j)
            if idx < bin_len:
                j[0] = int(r[:-1] + bin_msg[idx], 2)
                idx += 1
            if idx < bin_len:
                j[1] = int(g[:-1] + bin_msg[idx], 2)
                idx += 1
            if idx < bin_len:
                j[2] = int(b[:-1] + bin_msg[idx], 2)
                idx += 1
            else:
                break

    return image


def main():
    im_name = input("Enter the image name : ")
    im = cv2.imread(im_name)

    msg = input("Enter the message to be encrypted : ")
    encrypted_img = hide_msg(im, msg)

    new_img_name = input("Enter the new file name : ")
    cv2.imwrite(new_img_name, encrypted_img)


if __name__ == "__main__":
    main()
