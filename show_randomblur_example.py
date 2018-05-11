import pyblur
from PIL import Image
import os
import cv2
import numpy as np
from scipy.signal import convolve2d
from pyblur.LinearMotionBlur import LinearMotionBlur_random_kernel

def get_random_blur(img_src):
    img_np_blur = np.zeros(img_src.shape)
    blur_kernel = LinearMotionBlur_random_kernel()
    for i in range(3):
        img_np_blur[:, :, i] = convolve2d(img_np[:, :, i], blur_kernel, mode='same', fillvalue=255.0)
    img_np_blur=img_np_blur.astype('uint8')

    return img_np_blur[:,:,::-1]

prefix='/media/wei/DATA/Kinect_Deblur_Train_clearIM'

target_folder='/media/wei/DATA/Kinect_Deblur_Train_BlurIM'
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
imgs=os.listdir(prefix)
for impath in imgs:
    print(impath)
    img_pl=Image.open(os.path.join(prefix,impath))
    img_np = np.array(img_pl,dtype="float32")
    img_np_blur=get_random_blur(img_np)
    cv2.imwrite(os.path.join(target_folder, impath),img_np_blur)
    # img_show_buff=np.zeros((img_np.shape[0], img_np.shape[1]*2, 3))
    # img_show_buff[:,:img_np.shape[1],:]=img_np
    # img_show_buff[:,img_np.shape[1]:,:]=img_np_blur
    # img_show_buff=img_show_buff.astype('uint8')
    # img_show_buff=img_show_buff[:,:,::-1]
    # cv2.imshow('blur showcase', img_show_buff)
    # k = cv2.waitKey(0)
    # if k == 27:  # wait for ESC key to exit
    #     cv2.destroyAllWindows()
    #     break


'''def LinearMotionBlur_random_kernel():
    lineLengthIdx = np.random.randint(0, len(lineLengths))
    lineTypeIdx = np.random.randint(0, len(lineTypes))
    lineLength = lineLengths[lineLengthIdx]
    lineType = lineTypes[lineTypeIdx]
    lineAngle = randomAngle(lineLength)
    return LineKernel(lineLength, lineAngle, lineType)
def LinearMotionByKernel(img,kernel):
    imgarray = np.array(img, dtype="float32")
    #kernel = LineKernel(dim, angle, linetype)
    convolved = convolve2d(imgarray, kernel, mode='same', fillvalue=255.0).astype("uint8")
    img = Image.fromarray(convolved)
    return img
'''