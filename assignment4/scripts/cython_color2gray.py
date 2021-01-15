# UiO: IN4110
# Assignment 4
# Task 4.1
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


import cython_color2gray as ccg
import matplotlib.pyplot as plt
from time import time
import os
import cv2


t = []
g_image = None
for _ in range(3):
    image = cv2.imread('pictures/rain.jpg')
    t0 = time()
    g_image = ccg.cython_color2gray(image)
    t1 = time()
    t.append(t1-t0)

avg_t = (t[0]+t[1]+t[2])/3

# ####################################################### report
file_name = "cython_report_color2gray"

if os.path.isfile("reports/{}.txt".format(file_name)) is not True:
    os.system("touch reports/{}.txt".format(file_name))

log_file = open("reports/{}.txt".format(file_name), "a")
log_file.write("Timing: {}\n".format(file_name))
log_file.write("Average runtime running {} after 3 runs: {} s\n"
               .format(file_name, avg_t))

# getting result from other report 1
p = open('reports/python_report_color2gray.txt', 'rt')
a = p.readlines()
avg_p = float(a[-2].split()[7])
p.close()

# writing comparison 1
log_file.write(
    "Average runtime for running {} is {} faster "
    "or slower than python_color2gray.py\n"
    .format(file_name, avg_p / avg_t))

# getting result from other report 2
p = open('reports/numpy_report_color2gray.txt', 'rt')
a = p.readlines()
avg_p = float(a[-3].split()[7])
p.close()

# writing comparison 2
log_file.write(
    "Average runtime for running {} is {} faster "
    "or slower than numpy_color2gray.py\n"
        .format(file_name, avg_p / avg_t))

# getting result from other report 3
p = open('reports/numba_report_color2gray.txt', 'rt')
a = p.readlines()
avg_p = float(a[-4].split()[7])
p.close()

# writing comparison 3
log_file.write(
    "Average runtime for running {} is {} faster "
    "or slower than numba_color2gray.py\n"
        .format(file_name, avg_p / avg_t))

log_file.write("Timing performed using: 400x600x3")
log_file.close()

# ####################################################### testing
# saving the image
cv2.imwrite("pictures/cython_grayscale_image.jpg", g_image)

# plotting the image
plt.figure(figsize=(10, 20))
plt.imshow(g_image)
plt.show()
