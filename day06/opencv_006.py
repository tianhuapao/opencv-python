import cv2 as cv

'''
知识点：Look Up Table(LUT)查找表

- applyColorMap(src,dst,COLORMAP)
- src 表示输入图像
- dst 表示输出图像
- 匹配到的颜色LUT(Look Up Table),OpenCV支持13种颜色风格的查找表映射
'''
src = cv.imread("E:/gannimei/PycharmProjects/opencv_python/images/test.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
dst = cv.applyColorMap(src, cv.COLORMAP_PINK)
cv.imshow("output", dst)

# 伪色彩
image = cv.imread("E:/gannimei/PycharmProjects/opencv_python/images/test.jpg")
color_image = cv.applyColorMap(image, cv.COLORMAP_JET)
cv.imshow("image", image)
cv.imshow("color_image", color_image)
cv.waitKey(0)
cv.destroyAllWindows()




