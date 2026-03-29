Note:
This patch is intended for my customized Micropython + ulab build for X68000.
It includes additional features such as ndarray.repeat(), which are not enabled
in the default ulab configuration. Please apply it only to the corresponding
source tree.

注意:
このパッチは、X68000 用にカスタマイズした Micropython + ulab 向けです。
標準の ulab では有効になっていない ndarray.repeat() などの機能を含みます。
対応するソースツリーにのみ適用してください。

# micropython-x68k-ulab_patch

This repository stores the patch file (ulab_patch.diff) for my customized Micropython + ulab for X68000.

```
git clone https://github.com/yunkya2/micropython-x68k
cd micropython-x68k
git apply ../ulab_patch.diff
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
