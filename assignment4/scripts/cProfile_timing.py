# UiO: IN4110
# Assignment 4
# Task 4.0
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no

import scripts.test_slow_rectangle as tsr
import os
import numpy as np
import matplotlib.pyplot as plt
import cProfile
import pstats

profiler = cProfile.Profile()
elapsed_random_array = np.zeros(3)
elapsed_loop = np.zeros(3)
elapsed_snake_loop = np.zeros(3)
for i in range(3):

    profiler.enable()
    array = tsr.random_array(size=1e5, dim=3)
    a = tsr.loop(array)
    b = tsr.snake_loop(array)
    profiler.disable()

    status = pstats.Stats(profiler).stats

    values = []
    for e in status.items():
        values.append(e)

    elapsed_random_array[i] = values[-3][-1][-2]
    elapsed_loop[i] = values[-2][-1][-3]
    elapsed_snake_loop[i] = values[-1][-1][-3]


# writing report
if os.path.isfile("reports/cProfile_report.txt") is not True:
    os.system("touch reports/cProfile_report.txt")

log_file = open("reports/cProfile_report.txt", "a")

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

# comparison
manual_report = open("reports/manual_report.txt", "r")
l = manual_report.readlines()
get_name = l[-1].split()[3]
get_time = float(l[-1].split()[5])
manual_report.close()

cprofile_report = open("reports/cProfile_report.txt", "a")
cprofile_report.write("\nCompared to time() which got the function "
                      "{} as the slowest with: {} s"
                      .format(get_name, get_time))
cprofile_report.close()

# comparison 2
timeit_report = open("reports/timeit_report.txt", "r")
l = timeit_report.readlines()
get_name = l[-2].split()[3]
get_time = float(l[-2].split()[5])
timeit_report.close()

cprofile_report = open("reports/cProfile_report.txt", "a")
cprofile_report.write("\nCompared to timeit() which got the function "
                      "{} as the slowest with: {} s"
                      .format(get_name, get_time))
cprofile_report.close()
