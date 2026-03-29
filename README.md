# micropython-x68k-ulab_patch

This repository stores the patch file (rena_patch.diff) for my customized Micropython + ulab for X68000.

```
git clone https://github.com/yunkya2/micropython-x68k
cd micropython-x68k
git apply ../rena_patch.diff
```


```python
from ulab import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a)
print(a.flatten())
```
### Output
```
array([[1.0, 2.0, 3.0],
       [4.0, 5.0, 6.0]], dtype=float32)
array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float32)
```
