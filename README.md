## This patch is intended for the Micropython for the X68000 source tree only.

## micropython-x68k-ulab_patch
This repository stores the patch file (ulab_patch.diff) for my customized
Micropython for the X68000 + ulab build.

The patch enables several ulab features that are disabled in the default
configuration, and also includes a lightweight implementation of complex ndarray
(non‑NumPy compatible, designed specifically for the X68000 environment).

```
git clone https://github.com/yunkya2/micropython-x68k.git
cd micropython-x68k
git apply ulab_patch.diff
make -C mpy-cross && cd ports/x68k && make
```

## Important Notes

Do not use dtype inference.
arange, linspace, and implicit list→ndarray conversions do not work reliably on Micropython + ulab (X68000).
Always specify dtype explicitly when creating ndarrays.

Includes a lightweight complex ndarray implementation.
This is not NumPy compatible, but supports creation, indexing, printing, and vectorized abs() implemented in C.

Large arrays may fail due to memory constraints.
(Example: 256×256 OK, 512×512 → MemoryError)

## Tested features

ndarray creation (array, zeros, ones)

reshape / transpose

slicing

elementwise operations

reductions (sum, min, max, mean)

dot (matmul)

FFT

repeat

flatten

lightweight complex ndarray (non‑NumPy compatible)

memory limit behavior

## Sample

```
from ulab import numpy as np

a = np.array([[1, 2, 3],
[4, 5, 6]])

print(a)
print(a.flatten())
```

## Output
```
array([[1.0, 2.0, 3.0],
[4.0, 5.0, 6.0]], dtype=float32)
array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float32)
```
## The repository includes a comprehensive test script:

- sample/ulab_feature_test.py  
  A full feature test covering ndarray creation, reshape, slicing,
  reductions, dot, FFT, repeat, flatten, and the lightweight complex ndarray.

Please convert the file to Shift‑JIS before running it on the X68000.


### Encoding note

Sample Python scripts on GitHub are UTF‑8.
X68000 MicroPython does not fully support UTF‑8 multibyte characters.
Please convert .py files to Shift‑JIS before running them.


## このパッチは X68000 版 Micropython のソースツリー専用です。

# 日本語版 README

micropython-x68k-ulab_patch

このリポジトリは、X68000 用 Micropython に ulab を組み込んだ
カスタムビルド向けのパッチファイル（ulab_patch.diff）を公開しています。

```
git clone https://github.com/yunkya2/micropython-x68k.git
cd micropython-x68k
git apply ulab_patch.diff
make -C mpy-cross && cd ports/x68k && make
```

## 注意事項

dtype 推論は使用しないでください。
arange / linspace / 暗黙の list→ndarray 変換は X68000 版 Micropython + ulab では正しく動作しません。
ndarray 作成時は必ず dtype を明示してください。

complex ndarray は NumPy 互換ではありません。
X68000 上で動作するための軽量実装で、生成・アクセス・print 表示・abs() のベクトル化（C 実装）に対応します。

大規模配列はメモリ不足で失敗する可能性があります。
（例：256×256 は OK、512×512 は MemoryError）

## 動作確認済み

ndarray 基本操作

reshape / transpose

スライス

要素演算

各種集約関数

行列積

FFT

repeat / flatten

軽量 complex ndarray（独自実装）

メモリ限界テスト

## サンプル

```
from ulab import numpy as np

a = np.array([[1, 2, 3],
[4, 5, 6]])

print(a)
print(a.flatten())
```
## 以下の総合テストスクリプトを同梱しています：

- sample/ulab_feature_test.py  
  ndarray の生成、reshape、スライス、集約関数、行列積、FFT、repeat、
  flatten、軽量 complex ndarray など、全機能をまとめてテストできます。

X68000 で実行する前に Shift‑JIS に変換してください。


## 文字コードについて

GitHub 上のサンプルは UTF‑8 です。
X68000 版 Micropython は UTF‑8 のマルチバイト文字を完全には扱えません。
実行前に .py を Shift‑JIS に変換してください。
