# UiO: IN4110
# Assignment 4
# Task 4.3, 4.4, 4.5
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no


from numba import jit
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import argparse


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


class GrayScaleImage(Filters):

    def __init__(self, input_filename, output_filename=None):
        super().__init__(input_filename, output_filename)

    def run(self, implementation, plot=False, scale_factor=1.0):

        image = self._import()

        if (scale_factor > 0.0) and (scale_factor < 1.0):
            image = self.scale(image, scale_factor)

        elif scale_factor == 1.0:
            pass

        else:
            raise ValueError('Error: Scale factor can only '
                             'be 0 < factor <= 1')

        weights = np.array([[0.21, 0.72, 0.07],
                            [0.21, 0.72, 0.07],
                            [0.21, 0.72, 0.07]])

        new_image = None

        if implementation == "python":
            new_image = self.python_color2gray(image, weights)

        elif implementation == "numpy":
            new_image = self.numpy_color2gray(image, weights)

        elif implementation == "numba":
            new_image = self.numba_color2gray(image, weights)

        # # # Unable because of a lot of bugs
        # elif implementation == "cython":
        #     new_image = cython_color2gray(image)

        else:
            ValueError("Implementation not correct")

        if plot is not False:
            self._plot(new_image)

        if self.output_filename is not None:
            self._export(new_image)

        return new_image

    @staticmethod
    def python_color2gray(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        gray-scale image, using different weights and pure python.

        weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR gray-scale image
        """
        # creating n-array to store the new image
        new_image = np.empty(np.shape(image))

        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        # calculating the w_avg and setting up the grayscale image
        for x in range(h):  # 400
            for y in range(w):  # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    new_image[x, y, z] = w_avg

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image

    @staticmethod
    def numpy_color2gray(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        gray-scale image, using different weights and numpy.

        weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR gray-scale image
        """
        # mapping dot multiplication between channel and weights
        # laying the gray-scale values in a n-array image matrix
        new_image = np.dot(image, weights.T)

        # converting elements to uint8
        new_image = new_image.astype("uint8")

        return new_image

    def numba_color2gray(self, image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        gray-scale image, using different weights and numba.

        weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR gray-scale image
        """
        # creating n-array to store the new image
        new_image = np.empty(np.shape(image))

        new_image = self._use_numba(image, weights, new_image)

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image

    @staticmethod
    @jit
    def _use_numba(image, weights, new_image):
        """
        Isolating the for loop to be able to use numba and increase
        performance.
        """
        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        for x in range(h):  # 400
            for y in range(w):  # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    new_image[x, y, z] = w_avg

        return new_image


class SepiaScaleImage(Filters):

    def __init__(self, input_filename, output_filename=None):
        super().__init__(input_filename, output_filename)

    def run(self, implementation, plot=False,
            scale_factor=1.0, sepia_power=1.0):

        image = self._import()

        if (scale_factor > 0.0) and (scale_factor < 1.0):
            image = self.scale(image, scale_factor)

        elif scale_factor == 1.0:
            pass

        else:
            raise ValueError('Error: Scale factor can only '
                             'be 0 < factor <= 1')

        weights = np.array([[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]])

        if (sepia_power > 0.0) and (sepia_power <= 1.0):
            weights *= sepia_power

        else:
            raise ValueError('Error: Sepia power can only '
                             'be 0 < power <= 1')

        new_image = None

        if implementation == "python":
            new_image = self.python_color2sepia(image, weights)

        elif implementation == "numpy":
            new_image = self.numpy_color2sepia(image, weights)

        elif implementation == "numba":
            new_image = self.numba_color2sepia(image, weights)

        # # # Unable because of a lot of bugs
        # elif implementation == "cython":
        #     new_image = cython_color2sepia(image)

        else:
            ValueError("Implementation not correct")

        if plot is not False:
            self._plot(new_image)

        if self.output_filename is not None:
            self._export(new_image)

        return new_image

    @staticmethod
    def python_color2sepia(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        sepia-scale image, using different weights and pure python.

        weights:

            sepia_matrix = [[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]]

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR sepia-scale image
        """
        new_image = np.empty(np.shape(image))

        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        for x in range(h):  # 400
            for y in range(w):  # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    if w_avg >= 255:
                        w_avg = 255

                    new_image[x, y, z] = w_avg

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image

    @staticmethod
    def numpy_color2sepia(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        sepia-scale image, using different weights and numpy.

        weights:

            sepia_matrix = [[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]]

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR sepia-scale image
        """
        new_image = np.dot(image, weights.T)

        new_image[new_image > 255] = 255

        new_image = new_image.astype("uint8")

        return new_image

    @jit
    def numba_color2sepia(self, image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        sepia-scale image, using different weights and numba.

        weights:

            sepia_matrix = [[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]]

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR sepia-scale image
        """
        new_image = np.empty(np.shape(image))

        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        for x in range(h):  # 400
            for y in range(w):  # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    if w_avg >= 255:
                        w_avg = 255

                    new_image[x, y, z] = w_avg

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image


def main(e, f, o, i, p, sc, sp):
    """
    Takes the parse-arguments and runs the selected filter
    and implementation.

    :param e: str: Selecting the image filter/effect
                   among 'gray', 'sepia'.

    :param f: str: The path/filename of file to apply
                   filter to.

    :param o: str: The image-path/name to be exported.

    :param i: str: Selecting the implementation type
                   among 'python', 'numpy', 'numba'.

    :param p: bool: To plot the converted image.

    :param sc: float: The 0 < scale_factor <= 1, to
                      resize image.

    :param sp: float: The 0 < sepia_power <= 1, to
                      increase/decrease sepia filter.

    :return: Converted BGR ndarray image values.
    """
    if os.path.isfile('{}'.format(f)) is not True:
        raise ValueError('Error: Image does not exit.')

    if e == 'gray':
        gs = GrayScaleImage(input_filename=f, output_filename=o)
        return gs.run(implementation=i, plot=p, scale_factor=sc)

    elif e == 'sepia':
        ss = SepiaScaleImage(input_filename=f, output_filename=o)
        return ss.run(implementation=i, plot=p, scale_factor=sc, sepia_power=sp)


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(prog='instapy',
                                        description='Applies filters '
                                                    'to BGR images.')
    my_parser.version = '1.0'

    # The effect type to be used:
    my_parser.add_argument('-e', '-effect', action='store',
                           type=str, required=True,
                           choices=['gray', 'sepia'],
                           help="Selecting the image filter/effect among: "
                                "'gray', 'sepia'.")

    # The path/filename of file to apply filter to:
    my_parser.add_argument('-f', '-file', action='store',
                           type=str, required=True,
                           help='The path/filename of file to '
                                'apply filter to.')

    # The image-path/name to be exported:
    my_parser.add_argument('-o', '-out', action='store',
                           type=str, nargs=1,
                           help='The image-path/name to be exported.')

    # The implementation type to be used:
    my_parser.add_argument('-i', '-implement', action='store',
                           type=str, required=True,
                           choices=['python', 'numpy', 'numba'],
                           help="Selecting the implementation type "
                                "among 'python', 'numpy', 'numba'.")

    # To plot the converted image:
    my_parser.add_argument('-p', '-plot', action='store_true',
                           help='To plot the converted image.')

    # The 0 < scale_factor <= 1, to resize image:
    my_parser.add_argument('-sc', '-scale', action='store',
                           type=float, default=1.0,
                           help='The 0 < scale_factor <= 1, '
                                'to resize image.')

    # The 0 < sepia_power <= 1, to increase/reduce sepia filter:
    my_parser.add_argument('-sp', '-sepiapower', action='store',
                           type=float, default=1.0,
                           help='The 0 < sepia_power <= 1, to '
                                'increase/decrease sepia filter.')

    # Showing version of the package:
    my_parser.add_argument('-v', '-version', action='version')

    args = my_parser.parse_args()

    main(e=args.e, f=args.f, o=args.o, i=args.i,
         p=args.p, sc=args.sc, sp=args.sp)

    # python instapy.py -e sepia -f rain.jpg -i numpy -p
