import numpy
import cv2
import sys

def usage():
    print(" <imgname>")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    img = cv2.imread(sys.argv[1])
    cv2.imshow("lena", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
