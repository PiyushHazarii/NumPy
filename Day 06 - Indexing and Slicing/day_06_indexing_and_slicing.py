"""
Day 06 - Indexing and Slicing

Goal:
Select values, rows, columns, submatrices, and understand views vs copies.
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
    section("1-D Indexing")
    a = np.array([10, 20, 30, 40, 50])
    show("a", a)
    print("a[0]:", a[0])
    print("a[-1]:", a[-1])
    show("a[1:4]", a[1:4])
    show("a[::2]", a[::2])
    show("a[::-1]", a[::-1])

    section("2-D Indexing")
    b = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )
    show("b", b)
    print("b[1, 2]:", b[1, 2])
    show("b[0, :] - first row", b[0, :])
    show("b[:, 1] - second column", b[:, 1])
    show("b[0:2, 1:3] - submatrix", b[0:2, 1:3])

    section("Views vs Copies")
    original = np.array([1, 2, 3, 4, 5])
    view = original[1:4]
    copied = original[1:4].copy()

    show("original before changes", original)
    view[0] = 99
    show("original after changing view[0] = 99", original)

    copied[0] = 0
    show("copy after copied[0] = 0", copied)
    show("original after changing copied", original)

    print("np.shares_memory(original, view):", np.shares_memory(original, view))
    print("np.shares_memory(original, copied):", np.shares_memory(original, copied))

    section("Mini Practice")
    scores = np.array(
        [
            [70, 80, 90],
            [60, 75, 85],
            [95, 88, 92],
        ]
    )
    show("scores", scores)
    show("student 2 marks", scores[1, :])
    show("math column", scores[:, 0])
    show("first two students, last two subjects", scores[:2, 1:])


if __name__ == "__main__":
    main()
