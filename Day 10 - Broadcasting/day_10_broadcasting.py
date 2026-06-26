"""
Day 10 - Broadcasting

Goal:
Understand how NumPy combines arrays with different shapes without manual
loops or copies.
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
    section("Broadcasting Rules")
    print("1. Compare shapes from the right side.")
    print("2. Dimensions are compatible when they are equal or one of them is 1.")
    print("3. Missing dimensions are treated like 1 on the left.")

    section("Scalar + Array")
    a = np.array([1, 2, 3])
    show("a", a)
    show("a + 10", a + 10)

    section("Column Vector + Row Vector")
    column = np.array([[1], [2], [3]])
    row = np.array([10, 20, 30])

    show("column shape", column.shape)
    show("row shape", row.shape)
    show("column + row", column + row)
    print("Result shape:", (column + row).shape)

    section("Addition Table")
    col = np.arange(1, 6).reshape(5, 1)
    row = np.arange(1, 6)
    show("col", col)
    show("row", row)
    show("col + row", col + row)
    show("col * row", col * row)

    section("Real Example: Normalize Columns")
    data = np.array(
        [
            [10, 200],
            [20, 300],
            [30, 400],
        ],
        dtype=float,
    )
    column_means = data.mean(axis=0)
    centered = data - column_means

    show("data", data)
    show("column means", column_means)
    show("data - column_means", centered)

    section("Incompatible Shapes")
    left = np.ones((2, 3))
    right = np.ones((4,))
    print("left shape:", left.shape)
    print("right shape:", right.shape)
    try:
        left + right
    except ValueError as error:
        print("Broadcasting error:", error)


if __name__ == "__main__":
    main()
