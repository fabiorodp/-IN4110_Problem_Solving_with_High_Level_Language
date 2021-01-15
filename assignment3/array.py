# Assignment 3 - IN4110 - H2020 - UiO
# Exercise 3.2-6
# Author: Fábio Rodrigues Pereira - fabior@uio.no


class Array:
    # Assignment 3.3
    def __init__(self, shape, *values):
        """
        Make sure that you check that your array actually is an 
        array, which 
        means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array 
            with n 
            elements will have shape = (n,).
            *values: The values in the array. These should all be the same 
            data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with 
            the shape.
        """
        self.elements_type = type(values[0])
        self.shape = shape
        self.flat_values = values

        if len(self.shape) == 1:
            for i in values:

                if not isinstance(i, (bool, float, int)):
                    raise ValueError("All values can only be either" 
                                     " numeric or boolean.")

                elif not isinstance(i, self.elements_type):
                    raise ValueError("All values are not the same type.")

                elif len(values) != self.shape[0]:
                    raise ValueError("The number of values does not " 
                                     "fit with the shape.")

                else:
                    self.values = list(values)
        

        elif len(self.shape) == 2:
            n_rows = self.shape[0]  #nr of rows
            n_cols = self.shape[1]  #nr of cols

            if (n_rows * n_cols) == len(self.flat_values):

                for i in self.flat_values:
                    if not isinstance(i, (bool, float, int)):
                        raise ValueError("All values can only be either "
                                         "numeric or boolean.")

                    elif not isinstance(i, self.elements_type):
                        raise ValueError("All values are not the " 
                                         "same type.")


                self.values = [[0] * n_cols for _ in range(n_rows)]        
                count = 0

                for row in range(n_rows):
                    for col in range(n_cols):
                        self.values[row][col] = self.flat_values[count]
                        count += 1

            else:
                raise ValueError("The number of values does not fit with "
                                 "the shape.")
        

        elif len(self.shape) == 3:
            n_dims = self.shape[0]  #nr of dimens
            n_rows = self.shape[1]  #nr of rows
            n_cols = self.shape[2]  #nr of cols

            
            if (n_dims * n_rows * n_cols) == len(self.flat_values):

                for i in self.flat_values:
                    if not isinstance(i, (bool, float, int)):
                        raise ValueError("All values can only be either "
                                         "numeric or boolean.")

                    elif not isinstance(i, self.elements_type):
                        raise ValueError("All values are not the same "
                                         "type.")


                self.values = [ [[0] * n_cols for _ in range(n_rows)] \
                    for _ in range(n_dims) ]
                count = 0

                for dim in range(n_dims):
                    for row in range(n_rows):
                        for col in range(n_cols):
                            self.values[dim][row][col] = values[count]
                            count += 1

            else:
                raise ValueError("The number of values does not fit with "
                                 "the shape.")

    def __getitem__(self, args):
        '''
        Making the class 'Array' object subscriptable.
        '''
        if len(self.shape) == 1:  #for 1-dimensional
            return self.values[args]
        
        elif len(self.shape) == 2:  #for 2-dimensional
            if isinstance(args, tuple):
                row, col = args[0], args[1]
                return self.values[row][col]

            else:
                return self.values[args]
        
        elif len(self.shape) == 3:  #for n-dimensional
            dim, row, col = args[0], args[1], args[2]
            return self.values[dim][row][col]
        
        else:
            NotImplemented
            
    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        if len(self.shape) == 1:
            return "{}".format(self.values)
        
        elif len(self.shape) == 2:
            string_to_print = ""

            for line in self.values:
                string_to_print += " " + str(line) + "\n"
            return "[" + "{}".format(string_to_print)[1:-1] + "]"
        
        elif len(self.shape) == 3:
            string_to_print1 = ""

            for dimensions in self.values:
                string_to_print = ""
                
                for line in dimensions:
                    string_to_print += "   " + str(line) + "\n"
                
                string_to_print1 += "[" + string_to_print[3:-1] + "]" + "\n\n  "
            
            return "[ " + "{}".format(string_to_print1)[:-4] + " ]"
        
        else:
            NotImplemented

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied 
        arguments (specific data type or shape), it should return 
        NotImplemented.
        Args:
            other (Array, float, int): The array or number to add 
            element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        if isinstance(other, Array):
            if self.shape == other.shape:
                new_values = [(i + e) for i, e in \
                    zip(self.flat_values, other.flat_values)]

                return Array(self.shape, *new_values)

            else:
                raise ValueError("Erro: The Arrays have not the "
                                 "same shape.")

        elif isinstance(other, (float, int)):
            new_values = [(i + other) for i in self.flat_values]
            return Array(self.shape, *new_values)

        else:
            return NotImplemented

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied 
        arguments (specific data type or shape), it should return 
        NotImplemented.
        Args:
            other (Array, float, int): The array or number to add 
            element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return (self + other) if isinstance(other, (Array, float, int))\
            else NotImplemented

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied 
        arguments (specific data type or shape), it should 
        return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract 
            element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        if isinstance(other, Array):
            if self.shape == other.shape:
                new_values = [(i - e) for i, e in \
                    zip(self.flat_values, other.flat_values)]

                return Array(self.shape, *new_values)

            else:
                raise ValueError("Erro: The Arrays have "
                                 "not the same shape.")

        elif isinstance(other, (float, int)):
            new_values = [(i - other) for i in self.flat_values]
            return Array(self.shape, *new_values)

        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the 
        supplied arguments (specific data type or shape), it should 
        return NotImplemented.
        Args:
            other (Array, float, int): The array or number being 
            subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        return (self - other) if isinstance(other, (Array, float, int))\
            else NotImplemented

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the 
        supplied arguments (specific data type or shape), it should 
        return NotImplemented.
        Args:
            other (Array, float, int): The array or number to 
            multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        if isinstance(other, Array):
            if self.shape == other.shape:
                new_values = [(i * e) for i, e in \
                    zip(self.flat_values, other.flat_values)]

                return Array(self.shape, *new_values)

            else:
                raise ValueError("Erro: The Arrays have not "
                                    "the same shape.")

        elif isinstance(other, (float, int)):
            new_values = [(i * other) for i in self.flat_values]
            return Array(self.shape, *new_values)

        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the 
        supplied arguments (specific data type or shape), it should 
        return NotImplemented.
        Args:
            other (Array, float, int): The array or number to 
            multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        return (self * other) if isinstance(other, (Array, float, int))\
            else NotImplemented

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal. False otherwise.
        """
        if isinstance(other, Array):
            if self.shape != other.shape:
                return False
            else:
                return all(i == e for i, e in \
                    zip(self.flat_values, other.flat_values))
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not 
        match, this method should raise ValueError.
        Args:
            other (Array, float, int): The array or number to 
            compare with this array.
        Returns:
            Array: An array of booleans with True where the two 
            arrays match and False where they do not.
                   Or if `other` is a number, it returns True 
                   where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("The array's shapes are not equal")

            else:
                is_equal = [i == e for i, e in \
                    zip(self.flat_values, other.flat_values)]
                return Array(self.shape, *is_equal)

        elif isinstance(other, (int, float)):
            is_equal = [i == other for i in self.flat_values]
            return Array(self.shape, *is_equal)
        
        else:
            NotImplemented

    def mean(self):
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        if isinstance(self.flat_values[0], (int, float)):
            sum = 0
            for i in self.flat_values:
                sum += i

            mean = sum/len(self.flat_values)
            return mean

    def variance(self):
        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean( (x - x.mean())**2 )
        Returns:
            float: The mean of the array values.
        """
        if isinstance(self.flat_values[0], (int, float)):
            sum = 0
            for i in self.flat_values:
                sum += abs((i - self.mean())**2)

            var = sum/len(self.flat_values)
            return var

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for numeric data types.
        Returns:
            float: The value of the smallest element in the array.
        """
        if isinstance(self.flat_values[0], (int, float)):
            min_element = min(self.flat_values)
            return min_element
        else:
            raise ValueError("Only works for numeric data types.")
