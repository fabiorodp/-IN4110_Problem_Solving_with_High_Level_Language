# UiO: IN4110
# Assignment 4
# Task 4.0
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


from time import time
import scripts.test_slow_rectangle as tsr
import numpy as np
import os


elapsed_random_array = np.zeros(3)
elapsed_loop = np.zeros(3)
elapsed_snake_loop = np.zeros(3)
for i in range(3):

    t0 = time()
    array = tsr.random_array(1e5)
    t1 = time()
    elapsed_random_array[i] = t1 - t0

    t0 = time()
    filtered_array = tsr.snake_loop(array)
    t1 = time()
    elapsed_loop[i] = t1 - t0

    t0 = time()
    filtered_array_snack = tsr.loop(array)
    t1 = time()
    elapsed_snake_loop[i] = t1 - t0

# writing report
if os.path.isfile("reports/manual_report.txt") is not True:
    os.system("touch reports/manual_report.txt")

log_file = open("reports/manual_report.txt", "a")

log_file.write("\nTime Elapsed for random_array: {} s"
               .format(elapsed_random_array))
log_file.write("\nTime Elapsed for loop: {} s"
               .format(elapsed_loop))
log_file.write("\nTime Elapsed for snake_loop: {} s"
               .format(elapsed_snake_loop))

if (np.mean(elapsed_random_array) > np.mean(elapsed_loop)) \
        and (np.mean(elapsed_random_array) > np.mean(elapsed_snake_loop)):

    log_file.write("\nThe slowest is random_array with: {} avg s"
                   .format(np.mean(elapsed_random_array)))
    log_file.close()

elif (np.mean(elapsed_loop) > np.mean(elapsed_random_array)) \
        and (np.mean(elapsed_loop) > np.mean(elapsed_snake_loop)):

    log_file.write("\nThe slowest is loop with: {} avg s"
                   .format(np.mean(elapsed_loop)))
    log_file.close()

elif (np.mean(elapsed_snake_loop > elapsed_random_array)) \
        and (np.mean(elapsed_snake_loop > elapsed_loop)):

    log_file.write("\nThe slowest is snake_loop with: {} avg s"
                   .format(np.mean(elapsed_snake_loop)))
    log_file.close()
