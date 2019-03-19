import cv2 as cv

'''
颜色空间转转和图像保存
知识点：
1.色彩空间转换函数-cvtColor
 COLOR_BGR2GRAY = 6 彩色到灰度
 COLOR_GRAY2BGR = 8 灰度到彩色
 COLOR_BGR2HSV = 40 BGR到HSV
 COLOR_HSV2BGR = 54 HSV到BGR
2.图像保存 - imwrite
 第一个参数是图像保存路径
  第二个参数是图像保存对象
'''

src = cv.imread("E:\\gannimei\\PycharmProjects\\opencv_python\\day01\\test.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)  # 创建一个自适应窗口的图像
cv.imshow("input", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 图像转换成灰度模式
cv.imshow("gray", gray)
cv.waitKey(0)  # waitKey(0)表示阻塞等待用户键盘输入，用户按键盘任意键就会停止阻塞，继续执行直到程序正常退出！
cv.destroyAllWindows()
