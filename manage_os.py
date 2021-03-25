import os
import cv2
import fnmatch

rootPath = 'C:/Users/Tacha/VideoStreamingFlask/static/img/SIAM-ID/'
rootPath = 'C:/Users/Tacha/'
pattern = '*.ini'

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        img = os.path.join(root, filename)
        print( os.path.join(root, filename))

# image = cv2.imread(img)
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
