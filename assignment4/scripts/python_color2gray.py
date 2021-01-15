# UiO: IN4110
# Assignment 4
# Task 4.1
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


import numpy as np


def python_color2gray(n_array_image):
    """
    Convert an unsigned ndarray BGR image to an int8 ndarray
    gray-scale image, using different weights.

    weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

    :param n_array_image: An unsigned ndarray BGR image

    :return: An int8 ndarray BGR gray-scale image
    """
    # weights
    grayscale_matrix = np.array([[0.21, 0.72, 0.07],
                                 [0.21, 0.72, 0.07],
                                 [0.21, 0.72, 0.07]])

    # creating n-array to store the new image
    grayscale_image = np.empty(np.shape(n_array_image))

    # calculating the w_avg and setting up the grayscale image
    for x in range(grayscale_image.shape[0]):           # 400
        for y in range(grayscale_image.shape[1]):       # 600
            for z in range(grayscale_image.shape[2]):   # 3

                w_avg = 0
                for i in range(grayscale_image.shape[2]):

                    w_avg += n_array_image[x, y, i] * \
                             grayscale_matrix[z][i]

                grayscale_image[x, y, z] = w_avg

    # converting results to int
    grayscale_image = grayscale_image.astype("uint8")

    return grayscale_image


if __name__ == '__main__':
    from time import time
    import os
    import cv2

    t = []
    g_image = None
    for _ in range(3):
        image = cv2.imread('pictures/rain.jpg')
        t0 = time()
        g_image = python_color2gray(image)
        t1 = time()
        t.append(t1-t0)

    avg_t = (t[0]+t[1]+t[2])/3

    # ####################################################### report
    file_name = "python_report_color2gray"

    if os.path.isfile("reports/{}.txt".format(file_name)) is not True:
        os.system("touch reports/{}.txt".format(file_name))

    log_file = open("reports/{}.txt".format(file_name), "a")
    log_file.write("Timing: {}\n".format(file_name))
    log_file.write("Average runtime running {} after 3 runs: {} s\n"
                   .format(file_name, avg_t))
    log_file.write("Timing performed using: 400x600x3")
    log_file.close()

    # ####################################################### testing
    # saving the image
    cv2.imwrite("pictures/python_grayscale_image.jpg", g_image)

    # plotting the image
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 20))
    plt.imshow(g_image)
    plt.show()
