# UiO: IN4110
# Assignment 4
# Task 4.0
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


from timeit import timeit
import numpy as np
import os


elapsed_random_array = np.zeros(3)
elapsed_loop = np.zeros(3)
elapsed_snake_loop = np.zeros(3)
for i in range(3):

    elapsed_random_array[i] = \
        timeit(stmt="tsr.random_array(1e5)",
               setup="import test_slow_rectangle as tsr",
               number=1)

    elapsed_loop[i] = \
        timeit(stmt="tsr.snake_loop(array)",
               setup="import test_slow_rectangle as tsr; "
                     "array = tsr.random_array(1e5)",
               number=1)

    elapsed_snake_loop[i] = \
        timeit(stmt="tsr.loop(array)",
               setup="import test_slow_rectangle as tsr; "
                     "array = tsr.random_array(1e5)",
               number=1)

# writing report
if os.path.isfile("reports/timeit_report.txt") is not True:
    os.system("touch reports/manual_report.txt")

log_file = open("reports/timeit_report.txt", "a")

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

timeit_report = open("reports/timeit_report.txt", "a")
timeit_report.write("\nCompared to time() which got the function "
                    "{} as the slowest with: {} s"
                    .format(get_name, get_time))
timeit_report.close()
