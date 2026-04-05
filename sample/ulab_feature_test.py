# -*- coding: shift_jis -*-
# Comprehensive ulab test for Micropython for X68000 + ulab
# Covers ndarray creation, reshape, slicing, elementwise ops,
# reductions, matmul, FFT, repeat, flatten, and complex ndarray.

from ulab import numpy as np
from ulab import fft

def show(title, value):
    print("----", title, "----")
    print(value)

# 1. ndarray creation
a = np.array([[1, 2, 3],
              [4, 5, 6]], dtype=np.float32)
show("array a", a)

z = np.zeros((2, 3), dtype=np.float32)
o = np.ones((2, 3), dtype=np.float32)
show("zeros", z)
show("ones", o)

# 2. reshape / transpose
r = a.reshape((3, 2))
t = a.transpose()
show("reshape", r)
show("transpose", t)

# 3. slicing
s = a[:, 1]
show("slice a[:,1]", s)

# 4. elementwise operations
add = a + 10
mul = a * 2
show("a + 10", add)
show("a * 2", mul)

# 5. reductions
show("sum", np.sum(a))
show("min", np.min(a))
show("max", np.max(a))
show("mean", np.mean(a))

# 6. dot (matmul)
b = np.array([[1, 0, 1],
              [0, 1, 0]], dtype=np.float32)
d = np.dot(a, b)
show("dot(a, b)", d)

# 7. FFT
f = fft.fft(np.array([1, 2, 3, 4], dtype=np.float32))
show("fft([1,2,3,4])", f)

# 8. repeat
rep = np.repeat(np.array([1, 2, 3], dtype=np.float32), 3)
show("repeat", rep)

# 9. flatten
flat = a.flatten()
show("flatten", flat)

# 10. complex ndarray (lightweight implementation)
c = np.array([1+2j, 3+4j, -2+1j], dtype=np.complex)
show("complex array", c)

# vectorized abs()
abs_c = np.abs(c)
show("abs(complex)", abs_c)

print("All tests completed.")

