# IN3110-fabior
- **Author:** Fábio Rodrigues Pereira - fabior@uio.no
- **University:** University of Oslo
- **Course:** IN4110 - H2020

## Assignment 1:
- Basic git

## Assignment 2:
### Exercises 2.1 and extras are in file ./assignment2/2_1.sh:
- ***How to run the script?*** 
  - bash 2_1.sh [initial directory name] [destination directory name or new destination directory name] [file extension or all]

### Exercises 2.2 and 2.3 are in file ./assignment2/track.sh:
- This is a simple function to track activity time.
- ***How to run the function track?*** 
  - source track.sh
- ***Function's options:***
  - --help        # shows this help list"
  - --start       # starts a new tracking"
  - --stop        # stops a tracking"
  - --status      # shows the activity status"
  - --log         # shows the time log of a tracking"
  
## Assignment 3:
### Exercises 3.1 in file ./assignment3/wc.py:
- ***How to import the function?*** 
  - from wc import wc


- ***How to call the function?***
  - wc("file_name.extension" || "asterisk" || "asterisk.py")


### Exercises 3.2-6 in files ./assignment3/arra.py and ./assignment3/test_array.py:
- ***How to import the Array class?*** 
  - from array import Array
  
  
- ***How to call the Array class?*** 
  - Array(shape, *values) where shape and values are tuples. 
    - **For 1d:** shape = (nr_elements,) && values = (value_1, value_2, ...)
      - i.e.: str( Array((2,), 1, 2) ) = '[1, 2]'
    - **For 2d:** shape = (nr_rows, nr_cols) && values = (value_1, value_2, ...)
      - i.e.: str( Array((3,2), 8, 3, 4, 1, 6, 1) ) = '[[8, 3]\n [4, 1]\n [6, 1]]'
    - **For nd:** shape = (nr_dims, nr_rows, nr_cols) && values = (value_1, value_2, ...)
      - i.e.: str( Array((2, 2, 2), 1, 2, 3, 4, 5, 6, 7, 8) ) = '[ [[1, 2]\n   [3, 4]]\n\n  [[5, 6]\n   [7, 8]] ]'
      
      
- ***How to access a value in the array?***
  - **For 1d:** Array[element_idx_num]
    - i.e.: Array((2,), 1, 2)[1] = 2
  - **For 2d:** Array[row_nr][col_nr] || Array[row_nr, col_nr]
    - i.e.: Array((3,2), 8, 3, 4, 1, 6, 1)[1][0] = 4
    - or: Array((3,2), 8, 3, 4, 1, 6, 1)[1, 0] = 4
  - **For nd:** Array[dim_nr, row_nr, col_nr]
    - i.e.: Array((2, 2, 2), 1, 2, 3, 4, 5, 6, 7, 8)[1, 1, 0] = 7
    
    
  - ***Other methods in the Array class***
    - Works for 1, 2 and n-dimensional arrays:
      - Array.is_equal(other)
      - Array.mean()
      - Array.variance()
      - Array.min_element()

