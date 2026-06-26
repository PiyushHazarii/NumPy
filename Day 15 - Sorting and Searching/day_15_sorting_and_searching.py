"""
Day 15 - Sorting and Searching

Goal:
Sort arrays, find positions, locate values, and count unique values.
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
    section("Sorting 1-D Arrays")
    a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    show("a", a)
    show("np.sort(a) - sorted copy", np.sort(a))
    show("np.sort(a)[::-1] - descending", np.sort(a)[::-1])
    show("np.argsort(a) - indices that sort a", np.argsort(a))

    in_place = a.copy()
    in_place.sort()
    show("in_place after in_place.sort()", in_place)
    show("a is unchanged because we sorted a copy", a)

    section("Sorting 2-D Arrays")
    b = np.array([[3, 1, 2], [9, 4, 7]])
    show("b", b)
    show("np.sort(b, axis=1) - sort each row", np.sort(b, axis=1))
    show("np.sort(b, axis=0) - sort each column", np.sort(b, axis=0))

    section("Searching")
    sorted_arr = np.sort(a)
    show("sorted_arr", sorted_arr)
    print("np.argmin(a):", np.argmin(a))
    print("np.argmax(a):", np.argmax(a))
    show("np.where(a > 4)", np.where(a > 4))
    print("np.searchsorted(sorted_arr, 5):", np.searchsorted(sorted_arr, 5))
    show("np.nonzero(a)", np.nonzero(a))

    section("Unique Values")
    unique_values = np.unique(a)
    values, counts = np.unique(a, return_counts=True)
    show("np.unique(a)", unique_values)
    show("unique values", values)
    show("counts", counts)

    section("Mini Practice")
    names = np.array(["Raj", "Asha", "Mira", "Dev"])
    scores = np.array([72, 95, 88, 60])
    order = np.argsort(scores)[::-1]
    show("names sorted by highest score", names[order])
    show("scores sorted highest first", scores[order])


if __name__ == "__main__":
    main()
