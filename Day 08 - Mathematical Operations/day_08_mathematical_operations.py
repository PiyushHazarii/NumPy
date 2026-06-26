"""
Day 08 - Mathematical Operations

Goal:
Practice element-wise arithmetic, universal functions, and aggregations.
"""

try:
    import numpy as np
except ImportError as exc:
    raise SystemExit("NumPy is required. Install it with: pip install numpy") from exc


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def show(label, value):
    print(f"\n{label}:")
    print(value)


def main():
    section("Element-wise Arithmetic")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    show("a", a)
    show("b", b)
    show("a + b", a + b)
    show("a - b", a - b)
    show("a * b", a * b)
    show("a / b", a / b)
    show("a // b", a // b)
    show("a ** 2", a**2)
    show("a % 2", a % 2)
    show("np.add(a, b)", np.add(a, b))

    section("Universal Functions")
    values = np.array([1, 4, 9, 16], dtype=float)
    mixed_signs = np.array([-3, -1, 0, 2, 8])

    show("values", values)
    show("np.sqrt(values)", np.sqrt(values))
    show("np.exp(np.array([0, 1, 2]))", np.exp(np.array([0, 1, 2])))
    show("np.log(values)", np.log(values))
    show("np.log2(values)", np.log2(values))
    show("np.log10(values)", np.log10(values))
    show("np.sin(values)", np.sin(values))
    show("np.cos(values)", np.cos(values))
    show("np.ceil(np.array([1.2, 2.8]))", np.ceil(np.array([1.2, 2.8])))
    show("np.floor(np.array([1.2, 2.8]))", np.floor(np.array([1.2, 2.8])))
    show("np.round(np.array([1.2345, 6.789]), 2)", np.round(np.array([1.2345, 6.789]), 2))
    show("np.clip(mixed_signs, 0, 5)", np.clip(mixed_signs, 0, 5))
    show("np.sign(mixed_signs)", np.sign(mixed_signs))
    show("np.maximum(a, b)", np.maximum(a, b))
    show("np.minimum(a, b)", np.minimum(a, b))

    section("Aggregation Functions")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    show("matrix", matrix)
    print("np.sum(matrix):", np.sum(matrix))
    show("np.sum(matrix, axis=0) - column-wise", np.sum(matrix, axis=0))
    show("np.sum(matrix, axis=1) - row-wise", np.sum(matrix, axis=1))
    print("np.prod(matrix):", np.prod(matrix))
    show("np.cumsum(matrix)", np.cumsum(matrix))
    show("np.cumprod(np.array([1, 2, 3, 4]))", np.cumprod(np.array([1, 2, 3, 4])))
    show("np.diff(np.array([10, 15, 22, 30]))", np.diff(np.array([10, 15, 22, 30])))


if __name__ == "__main__":
    main()
