import cv2
import numpy as np

# 读取照片
image = cv2.imread('images/portrait.jpeg')

# 获取照片的宽度和高度
height, width = image.shape[:2]

# 计算圆的半径（取宽度和高度的最小值的一半）
radius = min(width, height) // 2

# 创建一个黑色的画布，大小与照片相同
canvas = np.zeros_like(image)

# 计算圆的中心点
center_x, center_y = width // 2, height // 2

# 在画布上画一个白色的圆形
cv2.circle(canvas, (center_x, center_y), radius, (255, 255, 255), -1)

# 将照片与画布进行按位与运算，保留圆形内部的原始图像
result = cv2.bitwise_and(image, canvas)

# 将圆圈外部区域设置为白色
result[np.where((result == [0, 0, 0]).all(axis=2))] = [255, 255, 255]


# 显示结果
cv2.imwrite('images/portrait1.jpg', result)