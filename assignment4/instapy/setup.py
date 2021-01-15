# UiO: IN4110
# Assignment 4
# Task 4.3
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no


import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='instapy',
    version='1.0',
    author="Fabio Rodrigues Pereira",
    author_email="fabior@uio.no",
    description="Filters for pictures.",
    url="https://github.uio.no/IN3110/IN3110-fabior",
    packages=setuptools.find_packages(),
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    scripts=["bin/instapy.py"]
)
