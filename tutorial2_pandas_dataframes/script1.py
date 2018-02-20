# Load libraries
import pandas as pd
import numpy as np

# A structured array
# numpy.ones(shape, dtype=None, order='C')[source]
#    Return a new array (ndarray (N-dimentional array)) of given shape and type, filled with ones.
my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))
# Print the structured array
print("printing foo: " + str(my_array['foo']))
print("printing bar: " + str(my_array['bar']))

# A record array
#  ndarray.view(dtype=None, type=None)
#    New view of array with the same data.
#    In this case, np.recarray is the dtype.  "an ndarray that allows field access using attributes."
my_array2 = my_array.view(np.recarray)
# Print the record array
print(my_array2.foo)
# okay, so my_array2 allows me to use the syntax my_array2.foo, whereas my_array requires me to use my_array['foo'].  Not clear why this matters so much.
print(my_array2.bar)
