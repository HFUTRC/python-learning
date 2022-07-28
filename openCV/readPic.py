import cv2
import matplotlib.pyplot as plt


# 使用函数cv2.imread(filepath,flags)读入一副图片
# filepath：要读入图片的完整路径
# flags：读入图片的标志
# cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道，可以直接写1
# cv2.IMREAD_GRAYSCALE：读入灰度图片，可以直接写0
# cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道，可以直接写-1

img = cv2.imread('1.jpg', 1)

# cv2.imshow("myWindow", img)
# # 这种方式只能通过按键关闭窗口，点击关闭按钮会导致程序无法正常结束
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 利用plt打开图像
# opencv读取颜色格式为bgr,plt显示为rgb格式，需要先对图片格式进行转换
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure("Image")  # 图像窗口名称

plt.imshow(img)
plt.axis('on')  # 关掉坐标轴为 off
plt.title('image')  # 图像题目
 
# 必须有这个，要不然无法显示
plt.show()


