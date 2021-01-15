# UiO: IN4110
# Assignment 4
# Task 4.2
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


import numpy as np


def python_color2sepia(n_array_image):
    """
    Convert an unsigned ndarray BGR image to an int8 ndarray
    sepia-scale image, using different weights.

    weights:

        sepia_matrix = [[0.131, 0.534, 0.272],
                        [0.168, 0.686, 0.349],
                        [0.189, 0.769, 0.393]]

    :param n_array_image: An unsigned ndarray BGR image

    :return: An int8 ndarray BGR sepia-scale image
    """
    # weights
    sepia_matrix = np.array([[0.131, 0.534, 0.272],
                             [0.168, 0.686, 0.349],     # BGR
                             [0.189, 0.769, 0.393]])

    # creating n-array to store the new image
    sepia_image = np.empty(np.shape(n_array_image))

    # calculating the w_avg and setting up the sepia-scale image
    for x in range(sepia_image.shape[0]):               # 400
        for y in range(sepia_image.shape[1]):           # 600
            for z in range(sepia_image.shape[2]):       # 3

                w_avg = 0
                for i in range(sepia_image.shape[2]):

                    w_avg += n_array_image[x, y, i] * \
                             sepia_matrix[z][i]

                if w_avg >= 255:
                    w_avg = 255

                sepia_image[x, y, z] = w_avg

    # converting results to int
    sepia_image = sepia_image.astype("uint8")

    return sepia_image


if __name__ == '__main__':
    from time import time
    import os
    import cv2

    t = []
    s_image = None
    for _ in range(3):
        image = cv2.imread('pictures/rain.jpg')
        t0 = time()
        s_image = python_color2sepia(image)
        t1 = time()
        t.append(t1 - t0)

    avg_t = (t[0] + t[1] + t[2]) / 3

    # ####################################################### report
    file_name = "python_report_color2sepia"

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
    cv2.imwrite("pictures/python_sepiascale_image.jpg", s_image)

    # plotting the image
    import matplotlib.pyplot as plt

    s_image = cv2.cvtColor(s_image, cv2.COLOR_BGR2RGB)  # RGB now
    plt.figure(figsize=(10, 20))
    plt.imshow(s_image)
    plt.show()
