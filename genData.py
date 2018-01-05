#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
def gen_rect():
    for i in xrange(1,51):
        img=np.zeros((128,128,3),np.uint8) # 生成空图像
        cv2.rectangle(img,(60-i%50,60-i%50),(68+i%50,68+i%50),(55,255,115),3)
        cv2.imwrite('./rect/'+str(i)+'r.jpg',img)
def gen_circle():
    for i in xrange(1,51):
        img=np.zeros((128,128,3),np.uint8) # 生成空图像
        cv2.circle(img,(64,64),i%50,(55,255,115),3)
        cv2.imwrite('./circle/'+str(i)+'c.jpg',img)
if __name__=='__main__':
    gen_rect()
    gen_circle()