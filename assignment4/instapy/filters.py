# UiO: IN4110
# Assignment 4
# Task 4.3
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no


import matplotlib.pyplot as plt
import numpy as np
import cv2


class Filters:

    def __init__(self, input_filename, output_filename=None):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def _plot(self, new_image):
        """Export the converted BGR image.

        :param new_image: ndarray with the converted BGR image values.
        """
        new_image = self._convert_BGR2RGB(new_image)
        plt.figure(figsize=(10, 20))
        plt.imshow(new_image)
        plt.show()

    def _import(self):
        """Import the original BGR image.

        :return: ndarray with the original BGR image values.
        """
        if isinstance(self.input_filename, np.ndarray):
            return self.input_filename

        else:
            return cv2.imread(self.input_filename)

    def _export(self, new_image):
        """Export the converted BGR image.

        :param new_image: ndarray with the converted BGR image values.
        """
        if self.output_filename is None:
            raise ValueError("Error: output_filename is not given."
                             "Please, use give_output_filename(name).")

        cv2.imwrite(self.output_filename, new_image)

    @staticmethod
    def _convert_BGR2RGB(img):
        """Convert BGR to RGB.

        :param img: ndarray to be converted from BGR to RGB.

        :return: ndarray with the converted RGB image values.
        """
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def give_output_filename(self, name):
        """Give the output file a name.

        :param name: str with path and name of the output image.
        """
        self.output_filename = name

    @staticmethod
    def scale(image, factor):
        """Scale the image by a factor.

        :param image: ndarray with the original BGR image.
        :param factor: float between 0 and 1 to scale the input image.

        :return: ndarray with the resized original BGR image values.
        """
        return cv2.resize(image, (0, 0), fx=factor, fy=factor)
