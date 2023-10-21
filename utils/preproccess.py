import cv2 as cv
import os
import numpy as np

def enhance_edge(image):
    # 边缘检测
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edge_output = cv.Canny(gray, 50, 150)
    dst = cv.bitwise_and(image, image, mask=edge_output)
    return dst

def enhance_contrast(image, brightness_factor, contrast_factor):
    # 调整亮度
    brightened = cv.convertScaleAbs(image, alpha=brightness_factor)
    # 调整对比度
    lab = cv.cvtColor(brightened, cv.COLOR_BGR2LAB)
    lab_planes = list(cv.split(lab))
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv.merge(lab_planes)
    contrasted = cv.cvtColor(lab, cv.COLOR_LAB2BGR)

    return contrasted

input_dir = "../data/images_pop_ups"
output_dir = "../data/images_pop_ups"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    # print(filename)

    # 在训练/预测前，对图像进行边缘检测和明暗对比度调整
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(input_dir, filename)
        image = cv.imread(image_path)


        image_canny = enhance_edge(image)

        kernel = np.ones((1,1), np.uint8)
        image_canny = cv.erode(image_canny, kernel)

        brightness_factor = 1
        contrast_factor = 1.5

        output_image = enhance_contrast(image_canny, brightness_factor, contrast_factor)

        output_path = os.path.join(output_dir, filename)
        cv.imwrite(output_path, output_image)







