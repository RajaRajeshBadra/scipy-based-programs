from scipy import linalg
import numpy as np

two_d_array = np.array([ [4,5], [3,2] ])
a=linalg.det( two_d_array )
b=linalg.inv( two_d_array )
print(a)
print(b)