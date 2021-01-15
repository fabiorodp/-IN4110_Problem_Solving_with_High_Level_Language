# UiO: IN4110
# Assignment 4
# Task 4.3
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


from instapy.grayscale_image import GrayScaleImage
from instapy.sepiascale_image import SepiaScaleImage
import numpy as np
import pytest


def test_color2gray():
    """Testing if the function makes the correct calculations."""
    np.random.seed(1)
    rand_img = np.random.randint(1, 255, size=(400, 600, 3))

    BGR = int(rand_img[0, 0, 0] * 0.21
              + rand_img[0, 0, 1] * 0.72
              + rand_img[0, 0, 2] * 0.07)

    gs = GrayScaleImage(input_filename=rand_img)

    python_gray_image = gs.run(implementation="python", plot=False)

    numpy_gray_image = gs.run(implementation="numpy", plot=False)

    numba_gray_image = gs.run(implementation="numba", plot=False)

    assert pytest.approx(BGR, python_gray_image[0, 0, 0])
    assert pytest.approx(BGR, numpy_gray_image[0, 0, 1])
    assert pytest.approx(BGR, numba_gray_image[0, 0, 2])
    assert np.allclose(python_gray_image, numpy_gray_image, atol=1)
    assert np.allclose(numpy_gray_image, numba_gray_image, atol=1)


def test_color2sepia():
    """Testing if the function makes the correct calculations."""
    np.random.seed(1)
    rand_img = np.random.randint(1, 255, size=(400, 600, 3))

    BGR = int(rand_img[0, 0, 0] * 0.131
              + rand_img[0, 0, 1] * 0.534
              + rand_img[0, 0, 2] * 0.272)

    sp = SepiaScaleImage(input_filename=rand_img)

    python_sepia_image = sp.run(implementation="python", plot=False)

    numpy_sepia_image = sp.run(implementation="numpy", plot=False)

    numba_sepia_image = sp.run(implementation="numba", plot=False)

    assert pytest.approx(BGR, python_sepia_image[0, 0, 0])
    assert pytest.approx(BGR, numpy_sepia_image[0, 0, 0])
    assert pytest.approx(BGR, numba_sepia_image[0, 0, 0])
    assert np.allclose(python_sepia_image, numpy_sepia_image, atol=1)
    assert np.allclose(numpy_sepia_image, numba_sepia_image, atol=1)
