# UiO: IN4110
# Assignment 4
# Task 4.4 and 4.5
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no


import argparse
import os
from instapy.grayscale_image import GrayScaleImage
from instapy.sepiascale_image import SepiaScaleImage


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
