# UiO: IN4110
# Assignment 4
# Task 4.2
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


import numpy as np


def numpy_color2sepia(n_array_image):
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
    # sepia weights matrix
    sepia_matrix = np.array([[0.131, 0.534, 0.272],
                             [0.168, 0.686, 0.349],  # BGR
                             [0.189, 0.769, 0.393]])

    # mapping dot multiplication between channel and weights.T
    # laying the sepia-scale values in a n-array image matrix
    sepia_image = n_array_image @ sepia_matrix.T

    # setting 255 if any element is greater than 255
    sepia_image[sepia_image > 255] = 255

    # converting elements to uint8
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
        s_image = numpy_color2sepia(image)
        t1 = time()
        t.append(t1 - t0)

    avg_t = (t[0] + t[1] + t[2]) / 3

    # ####################################################### report
    file_name = "numpy_report_color2sepia"

    if os.path.isfile("reports/{}.txt".format(file_name)) is not True:
        os.system("touch reports/{}.txt".format(file_name))

    log_file = open("reports/{}.txt".format(file_name), "a")
    log_file.write("Timing: {}\n".format(file_name))
    log_file.write("Average runtime running {} after 3 runs: {} s\n"
                   .format(file_name, avg_t))

    # getting result from other report
    p = open('reports/python_report_color2sepia.txt', 'rt')
    a = p.readlines()
    avg_p = float(a[-2].split()[7])
    p.close()

    # writing comparison
    log_file.write(
        "Average runtime running of {} is {} "
        "times faster or slower than python_color2sepia\n"
        .format(file_name, avg_p/avg_t))

    log_file.write("Timing performed using: 400x600x3")
    log_file.close()

    # ####################################################### testing
    # saving the image
    cv2.imwrite("pictures/numpy_sepiascale_image.jpg", s_image)

    # plotting the image
    import matplotlib.pyplot as plt

    s_image = cv2.cvtColor(s_image, cv2.COLOR_BGR2RGB)  # RGB now
    plt.figure(figsize=(10, 20))
    plt.imshow(s_image)
    plt.show()
