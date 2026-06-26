"""
Day 19 - NumPy vs Python Lists

Goal:
See the practical differences between Python lists and NumPy arrays.
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
    section("Data Types")
    python_list = [1, "two", 3.0]
    numpy_array = np.array([1, "two", 3.0])

    show("Python list with mixed values", python_list)
    show("NumPy array from mixed values", numpy_array)
    print("NumPy converted values to one common dtype:", numpy_array.dtype)

    section("Math Operations")
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    array_a = np.array([1, 2, 3])
    array_b = np.array([4, 5, 6])

    show("list_a + list_b gives concatenation", list_a + list_b)
    show("array_a + array_b gives element-wise addition", array_a + array_b)

    try:
        list_a + 10
    except TypeError as error:
        print("list_a + 10 error:", error)

    show("array_a + 10 works by broadcasting", array_a + 10)

    section("Dimensions")
    nested_list = [[1, 2, 3], [4, 5, 6]]
    matrix = np.array(nested_list)
    show("nested_list", nested_list)
    show("matrix", matrix)
    print("matrix.shape:", matrix.shape)
    show("matrix[:, 1] - easy column selection", matrix[:, 1])

    section("Fixed Size vs Dynamic Size")
    list_dynamic = [1, 2, 3]
    list_dynamic.append(4)
    show("list after append", list_dynamic)

    arr_fixed = np.array([1, 2, 3])
    arr_new = np.append(arr_fixed, 4)
    show("arr_fixed", arr_fixed)
    show("np.append(arr_fixed, 4) returns a new array", arr_new)

    section("Memory")
    many_numbers = np.arange(1_000_000, dtype=np.int32)
    print("NumPy stores 1,000,000 int32 numbers in bytes:", many_numbers.nbytes)
    print("Python lists store many separate Python objects, so overhead is much higher.")

    section("Linear Algebra")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    show("A @ B", A @ B)
    print("Python lists do not have built-in matrix multiplication like this.")


if __name__ == "__main__":
    main()
