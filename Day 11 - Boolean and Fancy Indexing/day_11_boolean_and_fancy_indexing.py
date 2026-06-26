"""
Day 11 - Boolean Indexing and Fancy Indexing

Goal:
Filter arrays with conditions and select values using index arrays.
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
    section("Boolean Indexing")
    a = np.array([10, 25, 3, 47, 8, 56])
    mask = a > 20

    show("a", a)
    show("mask = a > 20", mask)
    show("a[mask]", a[mask])
    show("a[a % 2 == 0] - even numbers", a[a % 2 == 0])
    show("a[(a > 10) & (a < 50)]", a[(a > 10) & (a < 50)])

    section("Setting Values with a Boolean Mask")
    changed = a.copy()
    changed[changed < 10] = 0
    show("changed after changed[changed < 10] = 0", changed)

    section("np.where")
    show("np.where(a > 20, a, 0)", np.where(a > 20, a, 0))
    show("np.where(a > 20, 'big', 'small')", np.where(a > 20, "big", "small"))

    section("Fancy Indexing in 1-D")
    values = np.array([10, 20, 30, 40, 50])
    show("values", values)
    show("values[[0, 2, 4]]", values[[0, 2, 4]])
    show("values[[1, 1, 3]] - duplicate indices are allowed", values[[1, 1, 3]])

    section("Fancy Indexing in 2-D")
    b = np.array(
        [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
    )
    show("b", b)
    show("b[[0, 2], [1, 0]]", b[[0, 2], [1, 0]])
    print("That means [b[0, 1], b[2, 0]].")

    section("np.ix_ for Row/Column Selection")
    rows_and_columns = np.ix_([0, 2], [0, 1])
    show("b[np.ix_([0, 2], [0, 1])]", b[rows_and_columns])

    section("Mini Practice")
    marks = np.array([45, 67, 89, 32, 76, 90])
    passed = marks >= 50
    show("marks", marks)
    show("passed mask", passed)
    show("passing marks", marks[passed])
    show("grade labels", np.where(marks >= 75, "A", np.where(marks >= 50, "B", "Fail")))


if __name__ == "__main__":
    main()
