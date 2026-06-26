"""
Day 04 - Array Creation Methods

Goal:
Practice the main ways to create NumPy arrays.
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
    section("zeros, ones, full, empty")
    show("np.zeros((3, 4))", np.zeros((3, 4)))
    show("np.ones((2, 3), dtype=int)", np.ones((2, 3), dtype=int))
    show("np.full((2, 2), 7)", np.full((2, 2), 7))

    empty = np.empty((2, 3))
    show("np.empty((2, 3)) - values are uninitialized", empty)
    print("Always fill an empty array before using its values.")

    section("Identity Matrices")
    show("np.eye(4)", np.eye(4))
    show("np.identity(3)", np.identity(3))

    section("arange and linspace")
    show("np.arange(0, 10, 2)", np.arange(0, 10, 2))
    show("np.arange(1.0, 2.0, 0.25)", np.arange(1.0, 2.0, 0.25))
    show("np.linspace(0, 1, 5)", np.linspace(0, 1, 5))
    show("np.linspace(0, 100, 11)", np.linspace(0, 100, 11))

    section("logspace and geomspace")
    show("np.logspace(0, 3, 4)", np.logspace(0, 3, 4))
    show("np.geomspace(1, 1000, 4)", np.geomspace(1, 1000, 4))

    section("From Existing Data")
    numbers = [1, 2, 3]
    arr = np.asarray(numbers)
    copied = np.copy(arr)
    from_bytes = np.frombuffer(b"\x01\x02\x03\x04", dtype=np.uint8)
    from_func = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)

    show("np.asarray([1, 2, 3])", arr)
    show("np.copy(arr)", copied)
    show("np.frombuffer(..., dtype=np.uint8)", from_bytes)
    show("np.fromfunction(lambda i, j: i + j, (3, 3))", from_func)

    section("Mini Practice")
    multiplication_table = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (5, 5), dtype=int)
    show("5x5 multiplication table", multiplication_table)


if __name__ == "__main__":
    main()
