# Exercises 4.0, 4.1, 4.2:

They are in the folder 'scripts/'.

# instapy package, exercises 4.3, 4.4 and 4.5:

They are in the folder 'instapy/'.

### Structure:

instapy/

|-- __init__.py

|-- README.md

|-- setup.py

|-- filters.py

|-- grayscale_image.py

|-- sepiascale_image.py

|-- instapy.py.py 

|   |bin/

|      |-- __init__.py 

|      |-- instapy.py 


### Usage:

instapy [-h] -e {gray,sepia} -f F [-o O] -i {python,numpy,numba} [-p] [-sc SC] [-sp SP] [-v]

Applies filters to BGR images.

### Arguments:

  -h, --help:               Show this help message and exit
  
  -e {gray,sepia}, -effect {gray,sepia}:    Selecting the image filter/effect among: 'gray', 'sepia'.
                        
  -f F, -file F:            The path/filename of file to apply filter to.
  
  -o O, -out O:             The image-path/name to be exported.
  
  -i {python,numpy,numba}, -implement {python,numpy,numba}: Selecting the implementation type among 'python', 'numpy', 'numba'.
                        
  -p, -plot:                To plot the converted image.
  
  -sc SC, -scale SC:        The 0 < scale_factor <= 1, to resize image.
  
  -sp SP, -sepiapower SP:   The 0 < sepia_power <= 1, to increase/decrease sepia filter.
                        
  -v, -version:             Show program's version number and exit
  
