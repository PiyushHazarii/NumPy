"""
Day 05 - Array Attributes

Goal:
Inspect arrays using ndim, shape, size, dtype, itemsize, nbytes, T, flat,
real, and imag.
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
    section("Basic Attributes")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    show("a", a)

    print("a.ndim:", a.ndim)
    print("a.shape:", a.shape)
    print("a.size:", a.size)
    print("a.dtype:", a.dtype)
    print("a.itemsize:", a.itemsize, "bytes per element")
    print("a.nbytes:", a.nbytes, "total bytes")

    section("Transpose")
    show("a.T", a.T)
    print("Original shape:", a.shape)
    print("Transposed shape:", a.T.shape)

    section("flat Iterator")
    print("Values from a.flat:")
    for value in a.flat:
        print(value, end=" ")
    print()

    section("Real and Imaginary Parts")
    complex_array = np.array([1 + 2j, 3 - 4j, 5 + 0j])
    show("complex_array", complex_array)
    show("complex_array.real", complex_array.real)
    show("complex_array.imag", complex_array.imag)

    section("Memory Example")
    # Before using Data Types, it's important to understand how they affect memory usage.
    float64_arr = np.ones((1000,), dtype=np.float64)
    float32_arr = np.ones((1000,), dtype=np.float32)
    print("float64 bytes:", float64_arr.nbytes)
    print("float32 bytes:", float32_arr.nbytes)
    print("float32 uses half the memory of float64 for the same number of values.")


if __name__ == "__main__":
    main()
