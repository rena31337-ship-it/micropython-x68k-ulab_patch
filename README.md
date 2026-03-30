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
git clone https://github.com/yunkya2/micropython-x68k.git
cd micropython-x68k
git apply ulab_patch.diff
make -C mpy-cross && cd ports/x68k && make
```
⚠️ mpy-cross のビルドについて（macOS / Fedora）
macOS（Clang）や一部の Linux 環境では、mpy-cross のビルド時に
コンパイラ警告がエラー扱いされて失敗する場合があります。

その場合は以下のように -Werror を無効化してください。

    make -C mpy-cross CFLAGS_EXTRA="-Wno-error"

⚠️ 注意：サンプルコードは UTF-8 になっているので、X68000 で実行する前に Shift-JIS に変換してください。

⚠️ Note: Sample Python scripts are stored as UTF-8 on GitHub.
X68000 MicroPython does not fully support UTF-8 multibyte characters, so
please convert .py files to Shift-JIS before running them on X68000.




Tested features:
- ndarray creation (array, zeros, ones)
- reshape, transpose
- slicing
- elementwise operations
- reductions (sum, min, max, mean)
- dot (matmul)
- FFT
- repeat
- flatten
- memory limit behavior

動作確認済み:
- ndarray 基本操作
- reshape / transpose
- スライス
- 要素演算
- 各種集約関数
- 行列積
- FFT
- repeat / flatten
- メモリ限界テスト

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
