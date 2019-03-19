import cv2 as cv

'''
OpenCV中图像像素读写操作
'''
src = cv.imread("E:\\gannimei\\PycharmProjects\\opencv_python\\images\\jianzu.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
# print(src.shape)
h, w, ch = src.shape
print("h, w, ch", h, w, ch)  # 输出图像的高、宽和通道
for row in range(h):  # 数组遍历
    for col in range(w):
        b, g, r = src[row, col]  # 这里src[row,col]表示图像中的一个像素，每个像素值都是一个三维向量组成的，b->红，g->绿，b->蓝色
        # print(r)
        b = 255-b
        g = 255-g
        r = 255-r
        src[row, col] = [b, g, r]
cv.imshow("output", src)
cv.waitKey(0)
cv.destroyAllWindows()
