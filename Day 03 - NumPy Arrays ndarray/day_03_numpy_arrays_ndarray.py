"""
Day 03 - NumPy Arrays - ndarray

Goal:
Understand 1-D, 2-D, and 3-D arrays, plus dtype and type casting.
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


def describe_array(name, array):
    show(name, array)
    print("ndim:", array.ndim)
    print("shape:", array.shape)
    print("dtype:", array.dtype)


def main():
    section("1-D Array")
    a = np.array([1, 2, 3, 4, 5])
    describe_array("a = np.array([1, 2, 3, 4, 5])", a)

    section("2-D Array (Matrix)")
    b = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
        ]
    )
    describe_array("b", b)
    print("b[0, 1] means row 0, column 1:", b[0, 1])

    section("3-D Array")
    c = np.array(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ]
    )
    describe_array("c", c)
    print("c[1, 0, 1] picks block 1, row 0, column 1:", c[1, 0, 1])

    section("Common Data Types")
    int_array = np.array([1, 2, 3], dtype=np.int32)
    unsigned_array = np.array([1, 2, 3], dtype=np.uint8)
    float_array = np.array([1.5, 2.5, 3.5], dtype=np.float64)
    complex_array = np.array([1 + 2j, 3 + 4j])
    bool_array = np.array([True, False, True])
    string_array = np.array(["a", "b", "numpy"])

    describe_array("int32 array", int_array)
    describe_array("uint8 array", unsigned_array)
    describe_array("float64 array", float_array)
    describe_array("complex array", complex_array)
    describe_array("bool array", bool_array)
    describe_array("string array", string_array)

    section("Type Casting with astype")
    original = np.array([1.2, 2.8, 3.9], dtype=np.float32)
    casted = original.astype(np.int64)

    describe_array("original float32", original)
    describe_array("casted int64", casted)
    print("Casting float to int removes the decimal part.")

    section("Why Same dtype Matters")
    mixed = np.array([1, 2.5, 3])
    describe_array("mixed = np.array([1, 2.5, 3])", mixed)
    print("NumPy converted all values to one common dtype.")


if __name__ == "__main__":
    main()
