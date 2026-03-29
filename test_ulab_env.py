# test_ulab_env4.py
import time

try:
    import ulab
    from ulab import numpy as np
except ImportError:
    print("ulab が import できませんでした。ビルド状態を確認してください。")
    raise SystemExit

# 表示用ヘルパ
def show(title, obj):
    print("===" + title + " ===")
    try:
        shp = obj.shape
    except:
        shp = None
    print("type:", type(obj), "shape:", shp)
    print(obj)
    print()

def safe_test(name, func):
    print("######## {} ########".format(name))
    t0 = time.ticks_ms()
    try:
        func()
        ok = True
    except MemoryError:
        print("MemoryError が発生しました。")
        ok = False
    except Exception as e:
        print("例外が発生しました:", e)
        ok = False
    t1 = time.ticks_ms()
    print("経過時間: {} ms".format(time.ticks_diff(t1, t0)))
    print()
    return ok

# 1. 基本 ndarray / shape / dtype
def test_basic_array():
    a = np.array([0, 1, 2, 3, 4])
    b = np.zeros(5)
    c = np.ones(5)
    show("a = array([0..4])", a)
    show("b = zeros(5)", b)
    show("c = ones(5)", c)

# 2. reshape / transpose
def test_2d_reshape():
    a = np.arange(12)
    show("arange(12)", a)
    m = a.reshape((3, 4))
    show("reshape(3,4)", m)
    mt = m.T
    show("transpose", mt)

# 3. 要素演算
def test_elementwise():
    x = np.linspace(0, 2.0, 9)
    show("x = linspace(0,2,9)", x)
    y = np.sin(x) + np.cos(x)
    show("y = sin(x)+cos(x)", y)
    z = x * x + 1.0
    show("z = x*x+1", z)

# 4. スライス
def test_slicing():
    a = np.arange(10)
    show("a", a)
    b = a[2:8]
    show("b = a[2:8]", b)
    c = a[::2]
    show("c = a[::2]", c)

# 5. reductions
def test_reductions():
    a = np.linspace(-1.0, 1.0, 11)
    show("a", a)
    print("sum(a) =", float(np.sum(a)))
    print("min(a) =", float(np.min(a)))
    print("max(a) =", float(np.max(a)))
    try:
        print("mean(a) =", float(np.mean(a)))
    except Exception as e:
        print("mean は未実装かもしれません:", e)
    print()

# 6. dot / matmul
def test_matmul():
    a = np.arange(6).reshape((2, 3))
    b = np.arange(6).reshape((3, 2))
    show("A (2x3)", a)
    show("B (3x2)", b)
    c = np.dot(a, b)
    show("C = dot(A,B)", c)

# 7. FFT
def test_fft_if_available():
    if hasattr(np, "fft") and callable(np.fft):
        x = np.sin(np.linspace(0, 2.0*np.pi, 32))
        show("x (time)", x)
        X = np.fft(x)
        show("X = fft(x)", X)
        return

    try:
        from ulab import fft
        x = np.sin(np.linspace(0, 2.0*np.pi, 32))
        show("x (time)", x)
        X = fft.fft(x)
        show("X = fft(x)", X)
        return
    except ImportError:
        pass

    print("この環境には FFT がありません。スキップします。")

# 8. ndarray メソッド repeat（あなたの環境用）
def test_repeat_method():
    a = np.array([1, 2, 3], dtype=np.int16)
    show("a", a)

    # スカラー repeat
    try:
        r1 = a.repeat(2)
        show("a.repeat(2)", r1)
    except Exception as e:
        print("a.repeat(2) ERROR:", e)

    # 配列 repeat
    try:
        r2 = a.repeat([1, 3, 2])
        show("a.repeat([1,3,2])", r2)
    except Exception as e:
        print("a.repeat([1,3,2]) ERROR:", e)

# 9. メモリ限界
def test_memory_limit():
    print("メモリ限界テスト: 2次元配列のサイズを増やしてみます。")
    n = 64
    while True:
        try:
            a = np.zeros((n, n))
            print("OK: zeros(({0},{0}))".format(n))
            n *= 2
            if n > 2048:
                print("n が 2048 を超えたので打ち切ります。")
                break
        except MemoryError:
            print("ここで MemoryError:", n, "x", n)
            break
    print()
# 10. flatten
def test_flatten():
    a = np.arange(12).reshape((3,4))
    show("a", a)

    # ndarray メソッド flatten
    try:
        f = a.flatten()
        show("a.flatten()", f)
    except Exception as e:
        print("a.flatten() ERROR:", e)

    # numpy.flatten が存在するかチェック
    if hasattr(np, "flatten"):
        try:
            f2 = np.flatten(a)
            show("np.flatten(a)", f2)
        except Exception as e:
            print("np.flatten(a) ERROR:", e)
    else:
        print("np.flatten はこの環境には存在しません。")

def main():
    tests = [
        ("basic_array", test_basic_array),
        ("2d_reshape", test_2d_reshape),
        ("elementwise", test_elementwise),
        ("slicing", test_slicing),
        ("reductions", test_reductions),
        ("matmul", test_matmul),
        ("fft_if_available", test_fft_if_available),
        ("repeat_method", test_repeat_method),
        ("memory_limit", test_memory_limit),
        ("flatten", test_flatten),
    ]
    for name, func in tests:
        safe_test(name, func)

if __name__ == "__main__":
    main()
