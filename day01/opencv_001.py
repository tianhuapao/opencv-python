import cv2 as cv

src = cv.imread("E:\\gannimei\\PycharmProjects\\opencv_python\\day01\\test.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)  # waitKey(0)表示阻塞等待用户键盘输入，用户按键盘任意键就会停止阻塞，继续执行直到程序正常退出！
cv.destroyAllWindows()
