# Assignment 3 - IN4110 - H2020 - UiO
# Exercise 3.2-6
# Author: Fábio Rodrigues Pereira - fabior@uio.no

from array import Array
import pytest


def test_str():
    '''
    Check that your print function actually returns the nice string:
    '''
    arr = Array((2,), 2, 1)  #1-dimensional
    assert str(arr) == "[2, 1]"

    arr = Array((3,2), 8, 3, 4, 1, 6, 1)  #2-dimensional
    assert str(arr) == '[[8, 3]\n [4, 1]\n [6, 1]]'
    assert arr[1][0] == 4
    assert arr[1,0] == 4

    arr = Array((2, 2, 2), 1, 2, 3, 4, 5, 6, 7, 8) #n-dimensional
    assert str(arr) == '[ [[1, 2]\n   [3, 4]]\n\n  [[5, 6]\n   [7, 8]] ]'
    assert arr[1, 1,0] == 7


def test_add():
    '''
    Verifying that adding to a 1d-array element-wise returns what 
    it’s supposed to:
    '''
    arr1 = Array((2,), 2, 1)
    arr2 = Array((2,), 1, 0)
    assert str(arr1 + arr2) == "[3, 1]"

    arr1 = Array((2,), 2, 1)
    arr2 = 0
    assert str(arr1 + arr2) == "[2, 1]"

    arr1 = Array((2,), 2.1, 1.1)
    arr2 = -0.1
    assert str(arr1 + arr2) == "[2.0, 1.0]"

    arr1 = Array((2,), 2, 2)
    arr2 = Array((1,), 1)
    with pytest.raises(ValueError):
        (arr1 + arr2)


def test_radd():
    '''
    Verifying that adding to a 1d-array element-wise returns what 
    it’s supposed to:
    '''
    arr1 = Array((2,), 3, 2)
    assert str(1 + arr1) == "[4, 3]"


def test_sub():
    '''
    Verifying that substracting from a 1d-array elementwise returns 
    what it’s supposed to
    '''
    arr1 = Array((2,), 2, 1)
    arr2 = Array((2,), 2, 2)
    assert str(arr1 - arr2) == "[0, -1]"

    arr1 = Array((2,), 2, 1)
    arr2 = 1
    assert str(arr1 - arr2) == "[1, 0]"

    arr1 = Array((2,), 2.2, -0.1)
    arr2 = -1
    assert str(arr1 - arr2) == "[3.2, 0.9]"

    arr1 = Array((2,), 2, 2)
    arr2 = Array((1,), 1)
    with pytest.raises(ValueError):
        (arr1 - arr2)


def test_rsub():
    '''
    Verifying that substracting from a 1d-array elementwise returns 
    what it’s supposed to
    '''
    arr1 = Array((5,), 1, 3, 2, 1, 2)
    assert str(1 - arr1) == "[0, 2, 1, 0, 1]"


def test_mul():
    '''
    Verifying that multiplying a 1d-array
    element-wise by a factor or other 1-d
    array returns what it’s supposed to
    '''
    arr1 = Array((2,), 2, 1)
    arr2 = Array((2,), 2, 2)
    assert str(arr1 * arr2) == "[4, 2]"

    arr1 = Array((2,), 2, 1)
    arr2 = 10
    assert str(arr1 * arr2) == "[20, 10]"

    arr1 = Array((2,), 2.2, -0.1)
    arr2 = -1
    assert str(arr1 * arr2) == "[-2.2, 0.1]"

    arr1 = Array((2,), 2, 2)
    arr2 = Array((1,), 1)
    with pytest.raises(ValueError):
        (arr1 * arr2)


def test_rmul():
    '''
    Verifying that multiplying a
    1d-array element-wise by a factor or other 1-d
    array returns what it’s supposed to
    '''
    arr1 = Array((2,), 1, 3)
    assert str(10 * arr1) == "[10, 30]"


def test_eq():
    '''
    Verifying that comparing two arrays (by ==)
    returns what it is supposed to - which should be
    a boolean.
    '''
    arr1 = Array((3,), 2, 3, 1)
    arr2 = Array((3,), 2, 3, 1)
    assert (arr1 == arr2) == True

    arr1 = Array((3,), 2, 3, 1)
    arr2 = Array((3,), 2, 3, 2)
    assert (arr1 == arr2) == False

    arr1 = Array((3,), 2, 3, 1)
    arr2 = Array((2,), 2, 3)
    assert (arr1 == arr2) == False

    arr1 = Array((3,), 2, 3, 1)
    arr2 = 1
    assert (arr1 == arr2) == False


def test_is_equal():
    '''
    Verifying that comparing a 1d-array element-wise
    to another array through is equal returns what
    it’s supposed to - which should be a boolean 
    array.
    '''
    arr1 = Array((2,), 2, 1)
    arr2 = 1
    assert str(arr1.is_equal(arr2)) == "[False, True]"

    arr1 = Array((2,), 2, 1)
    arr2 = Array((2,), 2, 1)
    assert str(arr1.is_equal(arr2)) == "[True, True]"

    arr1 = Array((2,), 2, 1)
    arr2 = Array((2,), 2, 2)
    assert str(arr1.is_equal(arr2)) == "[True, False]"


def test_mean():
    '''
    Verifying that the mean of the array is returned 
    correctly
    '''
    arr1 = Array((4,), 2, 4, 6, 8)
    assert arr1.mean() == 5

    arr1 = Array((2,), 5, 5)
    assert arr1.mean() == 5


def test_var():
    '''
    Verifying that the variance of the array is returned correctly
    '''
    arr1 = Array((4,), 2, 4, 6, 8)
    assert arr1.variance() == 5

    arr1 = Array((4,), 2, 3, 6, 8)
    assert arr1.variance() == 5.6875


def test_min_element():
    '''
    Verifying that the the element returned by min 
    element is the ”smallest” one in the array
    '''
    arr1 = Array((4,), 2, 4, 6, 8)
    assert arr1.min_element() == 2

    arr1 = Array((4,), 2, 3, 6, -8)
    assert arr1.min_element() == -8


def test_2d_add():
    '''
    Verifying that adding to a 2d-array element-wise returns what 
    it’s supposed to:
    '''
    arr1 = Array((2,5), 2, 1, 0, -1, 0, 5, 0, 0, 0, 0)
    arr2 = Array((2,5), 2, 1, 0, -1, 0, 5, 0, 0, 0, 0)
    assert str(arr1 + arr2) == \
        '[[4, 2, 0, -2, 0]\n [10, 0, 0, 0, 0]]'
    
    arr1 = Array((2,2), 2, 1, 0, -1)
    assert str(arr1 + 10) == "[[12, 11]\n [10, 9]]"

    arr1 = Array((2,2), 2, 2, 0, 0)
    arr2 = Array((2,), 2, 2)
    with pytest.raises(ValueError):
        (arr1 + arr2)


def test_2d_radd():
    '''
    Verifying that adding to a 2d-array element-wise returns what 
    it’s supposed to:
    '''
    arr1 = Array((2,2), 2, 1, 0, -1)
    assert str(10 + arr1) == "[[12, 11]\n [10, 9]]"


def test_2d_sub():
    '''
    Verifying that substracting from a 2d-array elementwise returns 
    what it’s supposed to
    '''
    arr1 = Array((2,3), 2, 1, 0, -1, 0, 5)
    arr2 = Array((2,3), 2, 1, 0, -1, 0, 5)
    assert str(arr1 - arr2) == '[[0, 0, 0]\n [0, 0, 0]]'
    
    arr1 = Array((2,2), 2, 1, 0, -1)
    assert str(arr1 - 10) == "[[-8, -9]\n [-10, -11]]"

    arr1 = Array((2,2), 2, 2, 0, 0)
    arr2 = Array((2,), 2, 2)
    with pytest.raises(ValueError):
        (arr1 - arr2)


def test_2d_rsub():
    '''
    Verifying that substracting from a 2d-array elementwise returns 
    what it’s supposed to
    '''
    arr1 = Array((2,2), 2, 1, 0, -1)
    assert str(10 - arr1) == "[[-8, -9]\n [-10, -11]]"


def test_2d_mul():
    '''
    Verifying that multiplying a 2d-array
    element-wise by a factor or other 1-d
    array returns what it’s supposed to
    '''
    arr1 = Array((2,3), 2, 1, 0, -1, 0, 5)
    arr2 = Array((2,3), 2, 1, 0, -1, 0, 5)
    assert str(arr1 * arr2) == '[[4, 1, 0]\n [1, 0, 25]]'
    
    arr1 = Array((2,2), 2, 1, 0, -1)
    assert str(arr1 * 10) == "[[20, 10]\n [0, -10]]"

    arr1 = Array((2,2), 2, 2, 0, 0)
    arr2 = Array((2,), 2, 2)
    with pytest.raises(ValueError):
        (arr1 * arr2)


def test_2d_rmul():
    '''
    Verifying that multiplying a
    1d-array element-wise by a factor or other 1-d
    array returns what it’s supposed to
    '''
    arr1 = Array((2,2), 2, 1, 0, -1)
    assert str(10 * arr1) == "[[20, 10]\n [0, -10]]"


def test_2d_eq():
    '''
    Verifying that comparing two arrays (by ==)
    returns what it is supposed to - which should be
    a boolean.
    '''
    arr1 = Array((2,2), 2, 3, 1, 1)
    arr2 = Array((2,2), 2, 3, 1, 1)
    assert (arr1 == arr2) == True

    arr1 = Array((2,2), 2, 3, 1, 1)
    arr2 = Array((2,2), 2, 3, 2, 1)
    assert (arr1 == arr2) == False

    arr1 = Array((2,2), 2, 3, 1,1)
    arr2 = Array((2,1), 2, 3)
    assert (arr1 == arr2) == False

    arr1 = Array((2,2), 2, 3, 1,1)
    arr2 = 1
    assert (arr1 == arr2) == False


def test_2d_is_equal():
    '''
    Verifying that comparing a 1d-array element-wise
    to another array through is equal returns what
    it’s supposed to - which should be a boolean 
    array.
    '''
    arr1 = Array((2,2), 2, 1, 1, 1)
    assert str(arr1.is_equal(1)) == \
        "[[False, True]\n [True, True]]"

    arr1 = Array((2,2), 2, 1, 1, 1)
    arr2 = Array((2,2), 2, 1, 1, 1)
    assert str(arr1.is_equal(arr2)) == \
        "[[True, True]\n [True, True]]"

    arr1 = Array((2,2), 2, 1, 1, 1)
    arr2 = Array((2,2), 2, 2, 1 , 1)
    assert str(arr1.is_equal(arr2)) == \
        "[[True, False]\n [True, True]]"


def test_2d_mean():
    '''
    Verifying that the mean of the array is returned 
    correctly
    '''
    arr1 = Array((2,2), 2, 2, 1, 1)
    assert arr1.mean() == 1.5


def test_2d_var():
    '''
    Verifying that the variance of the array is returned correctly
    '''
    arr1 = Array((2,2), 2, 2, 1, 1)
    assert arr1.variance() == 0.25


def test_2d_min_element():
    '''
    Verifying that the the element returned by min 
    element is the ”smallest” one in the array
    '''
    arr1 = Array((2,2), 2, 4, 6, 8)
    assert arr1.min_element() == 2

    arr1 = Array((2,2), 2, 3, 6, -8)
    assert arr1.min_element() == -8

def test_nd_add():
    '''
    Verifying that adding to a nd-array element-wise returns what 
    it’s supposed to:
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    arr2 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert str(arr1 + arr2) == \
        "[ [[2]\n   [4]]\n\n  [[6]\n   [8]]\n\n  [[10]\n   [12]] ]"
    
    assert str(arr1 + 1) == \
        "[ [[2]\n   [3]]\n\n  [[4]\n   [5]]\n\n  [[6]\n   [7]] ]"

    arr2 = Array((2,), 2, 2)
    with pytest.raises(ValueError):
        (arr1 + arr2)


def test_nd_radd():
    '''
    Verifying that adding to a nd-array element-wise returns what it’s supposed to:
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert str(1 + arr1) == \
        "[ [[2]\n   [3]]\n\n  [[4]\n   [5]]\n\n  [[6]\n   [7]] ]"


def test_nd_sub():
    '''
    Verifying that substracting from a nd-array elementwise returns what it’s supposed to
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    arr2 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert str(arr1 - arr2) == \
        "[ [[0]\n   [0]]\n\n  [[0]\n   [0]]\n\n  [[0]\n   [0]] ]"
    
    assert str(arr1 - 1) == \
        "[ [[0]\n   [1]]\n\n  [[2]\n   [3]]\n\n  [[4]\n   [5]] ]"

    arr2 = Array((2,), 2, 2)
    with pytest.raises(ValueError):
        (arr1 - arr2)


def test_nd_rsub():
    '''
    Verifying that substracting from a nd-array elementwise returns what it’s supposed to
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert str(1 - arr1) == \
        "[ [[0]\n   [1]]\n\n  [[2]\n   [3]]\n\n  [[4]\n   [5]] ]"


def test_nd_mul():
    '''
    Verifying that multiplying a nd-array
    element-wise by a factor or other 1-d
    array returns what it’s supposed to
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    arr2 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert str(arr1 * arr2) == \
        "[ [[1]\n   [4]]\n\n  [[9]\n   [16]]\n\n  [[25]\n   [36]] ]"
    
    assert str(arr1 * 2) == \
        "[ [[2]\n   [4]]\n\n  [[6]\n   [8]]\n\n  [[10]\n   [12]] ]"

    arr2 = Array((2,), 2, 2)
    with pytest.raises(ValueError):
        (arr1 * arr2)


def test_nd_rmul():
    '''
    Verifying that multiplying a
    1d-array element-wise by a factor or other 1-d
    array returns what it’s supposed to
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert str(2 * arr1) == \
        "[ [[2]\n   [4]]\n\n  [[6]\n   [8]]\n\n  [[10]\n   [12]] ]"


def test_nd_eq():
    '''
    Verifying that comparing two arrays (by ==)
    returns what it is supposed to - which should be
    a boolean.
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    arr2 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert (arr1 == arr2) == True

    arr2 = Array((3,2,1), 1, 2, 3, 4, 5, 7)
    assert (arr1 == arr2) == False

    arr2 = Array((2,1), 2, 3)
    assert (arr1 == arr2) == False

    assert (arr1 == 1) == False


def test_nd_is_equal():
    '''
    Verifying that comparing a 1d-array element-wise
    to another array through is equal returns what
    it’s supposed to - which should be a boolean 
    array.
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert str(arr1.is_equal(2)) == \
        '[ [[False]\n   [True]]\n\n  [[False]\n   [False]]\n\n  [[False]\n   [False]] ]'

    arr2 = Array((3,2,1), 8, 7, 6, 5, 4, 6)
    assert str(arr1.is_equal(arr2)) == \
        '[ [[False]\n   [False]]\n\n  [[False]\n   [False]]\n\n  [[False]\n   [True]] ]'


def test_nd_mean():
    '''
    Verifying that the mean of the array is returned 
    correctly
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert arr1.mean() == 3.5


def test_nd_var():
    '''
    Verifying that the variance of the array is returned correctly
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert arr1.variance() == 2.9166666666666665


def test_nd_min_element():
    '''
    Verifying that the the element returned by min 
    element is the ”smallest” one in the array
    '''
    arr1 = Array((3,2,1), 1, 2, 3, 4, 5, 6)
    assert arr1.min_element() == 1
