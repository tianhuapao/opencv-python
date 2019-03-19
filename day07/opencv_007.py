import cv2 as cv
import numpy as np

'''
知识点： 像素操作之逻辑操作
- bitwise_and
- bitwise_xor
- bitwise_or
上面三个类似，都是针对两张图像的位操作

- bitwise_not
针对输入图像, 图像取反操作，二值图像分析中经常用
'''
#  创建第一幅图像
src1 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src1[100:200, 100:200, 1] = 255
src1[100:200, 100:200, 2] = 255
cv.imshow("input1", src1)

#  创建第二幅图像
src2 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src2[150:250, 150: 250, 2] = 255
cv.imshow("input2", src2)

dst1 = cv.bitwise_and(src1, src2)
dst2 = cv.bitwise_xor(src1, src2)
dst3 = cv.bitwise_or(src1, src2)

cv.imshow("dst1", dst1)
cv.imshow("dst2", dst2)
cv.imshow("dst3", dst3)

src = cv.imread("E:\\gannimei\\PycharmProjects\\opencv_python\\images\\meinv.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
dst = cv.bitwise_not(src)
cv.imshow("dst", dst)


cv.waitKey(0)
cv.destroyAllWindows()
