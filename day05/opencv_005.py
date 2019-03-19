import cv2 as cv
import numpy as np

'''
OpenCV中像素算术操作

像素算术操作
+加add、-减subtract、*乘multiply、/除divide
注意点：图像的数据类型、通道数目、大小必须相同
'''

src1 = cv.imread("E:/gannimei/PycharmProjects/opencv_python/images/LinuxLogo.jpg")
src2 = cv.imread("E:/gannimei/PycharmProjects/opencv_python/images/WindowsLogo.jpg")
cv.imshow("input1", src1)
cv.imshow("input2", src2)
h, w, ch = src1.shape
print("h, w, ch", h, w, ch)

# 加法操作
add_result = np.zeros(src1.shape, src1.dtype)
cv.add(src1, src2, add_result)
cv.imshow("add_result", add_result)

# 减法操作
sub_result = np.zeros(src1.shape, src2.dtype)
cv.subtract(src1, src2, sub_result)
cv.imshow("sub_result", sub_result)

# 乘法操作
mul_result = np.zeros(src1.shape, src1.dtype)
cv.multiply(src1, src2, mul_result)
cv.imshow("mul_result", mul_result)

# 除法操作
div_result = np.zeros(src1.shape, src1.dtype)
cv.divide(src1, src2, div_result)
cv.imshow("div_result", div_result)

cv.waitKey(0)
cv.destroyAllWindows()
