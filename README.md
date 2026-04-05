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
git apply --whitespace=fix ulab_patch.patch
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

Tested features

- ndarray creation (array, zeros, ones)
- slicing
- elementwise operations
- reductions (sum, min, max, mean)
- dot (matmul)
- FFT
- flatten
- lightweight complex ndarray (non‑NumPy compatible)
- memory limit behavior

Not supported on the X68000 port of ulab:

- ndarray.reshape()
- transpose()
- repeat()

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

  sample/ulab_feature_test.py  
  A full feature test covering ndarray creation, slicing,
  reductions, dot, FFT, flatten, and the lightweight complex ndarray.

## Note:
 The X68000 port of ulab does not implement the ndarray.reshape() method.
 Calling a.reshape(...) will always raise an error on this platform.
 Only the functional form np.reshape() exists, and even that supports
 only limited use cases (mainly flattening to 1D).


### Encoding note

Sample Python scripts on GitHub are UTF‑8.
X68000 MicroPython does not fully support UTF‑8 multibyte characters.
Please convert .py files to Shift‑JIS before running them.

### Build notes (Mac / Linux)

Depending on your compiler, you may need to disable some warnings:

- macOS (Clang):
  make CFLAGS_EXTRA="-Wno-error"

- Fedora (GCC):
  make CFLAGS_EXTRA="-Wno-error=maybe-uninitialized"

- WSL2 Ubuntu:
  No special flags required.


## このパッチは X68000 版 Micropython のソースツリー専用です。

# 日本語版 README

micropython-x68k-ulab_patch

このリポジトリは、X68000 用 Micropython に ulab を組み込んだ
カスタムビルド向けのパッチファイル（ulab_patch.diff）を公開しています。

```
git clone https://github.com/yunkya2/micropython-x68k.git
cd micropython-x68k
git apply --whitespace=fix ulab_patch.patch
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

動作確認済み

- ndarray 基本操作
- スライス
- 要素演算
- 各種集約関数
- 行列積
- FFT
- flatten
- 軽量 complex ndarray（独自実装）
- メモリ限界テスト

X68000 版 ulab では未実装:

- ndarray.reshape()
- transpose()
- repeat()

## サンプル

```
from ulab import numpy as np

a = np.array([[1, 2, 3],
[4, 5, 6]])

print(a)
print(a.flatten())
```
## 以下の総合テストスクリプトを同梱しています：

  sample/ulab_feature_test.py  
  ndarray の生成、スライス、集約関数、行列積、FFT、
  flatten、軽量 complex ndarray など、主要な機能をまとめてテストできます。

## 注意:
X68000 版 ulab には ndarray.reshape() メソッドが実装されていません。
そのため a.reshape(...) を呼び出すと必ずエラーになります。
利用できるのは関数版の np.reshape() のみですが、
こちらも 1 次元への変換など、ごく限られた用途にしか対応していません。


## 文字コードについて

GitHub 上のサンプルは UTF‑8 です。
X68000 版 Micropython は UTF‑8 のマルチバイト文字を完全には扱えません。
実行前に .py を Shift‑JIS に変換してください。

ビルドオプションについて（macOS / Linux）
使用しているコンパイラによっては、
Micropython のビルド時に警告が多数表示される場合があります。
これらは動作に影響しませんが、ビルドを通すために
以下のオプションを追加する必要があります。

-macOS（Clang）

make CFLAGS_EXTRA="-Wno-error"

-Fedora（GCC）

make CFLAGS_EXTRA="-Wno-error=maybe-uninitialized"

-WSL2 Ubuntu（GCC）  
特別なオプションは不要です。

※ macOS や Fedora では、Micropython 本体のコードに対して
　Clang / GCC が厳しく警告を出すことがありますが、
　これらは無害であり、ビルドや動作には影響しません。
