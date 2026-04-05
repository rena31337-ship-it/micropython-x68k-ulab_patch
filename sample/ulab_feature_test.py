# -*- coding: shift_jis -*-
from ulab import numpy as np
from ulab import fft

def show(title, value):
    print("----", title, "----")
    print(value)

# 1. ndarray creation
a = np.array([[1, 2, 3],
              [4, 5, 6]], dtype=float)
show("array a", a)

# 2. zeros / ones (2D arrays must be created from list-of-lists)
z = np.array([[0, 0, 0],
              [0, 0, 0]], dtype=float)
o = np.array([[1, 1, 1],
              [1, 1, 1]], dtype=float)
show("zeros", z)
show("ones", o)

# 3. reshape (ndarray method version)
# Note:
# The X68000 port of ulab does not implement the ndarray.reshape() method.
# Calling a.reshape(...) will always raise an error on this platform.
# Only the functional form np.reshape() exists, and it supports only
# limited use cases (mainly flattening to 1D).
# r = a.reshape(3, 2)
# show("reshape", r)

# 4. slicing
s = a[:2]
show("slice a[:2]", s)

# 5. elementwise operations
add = a + 10
mul = a * 2
show("a + 10", add)
show("a * 2", mul)

# 6. reductions
show("sum", np.sum(a))
show("min", np.min(a))
show("max", np.max(a))
show("mean", np.mean(a))

# 7. dot（形状を合わせた 2×3 × 3×2）
b = np.array([[1, 0],
              [0, 1],
              [1, 0]], dtype=float)
d = np.dot(a, b)
show("dot(a, b)", d)

# 8. FFT
f = fft.fft(np.array([1, 2, 3, 4], dtype=float))
show("fft([1,2,3,4])", f)

# 9. flatten
flat = a.flatten()
show("flatten", flat)

# 10. complex ndarray
c = np.array([1+2j, 3+4j, -2+1j], dtype=complex)
show("complex array", c)
show("abs(complex)", np.abs(c))

print("All tests completed.")

