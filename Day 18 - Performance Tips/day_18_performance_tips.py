"""
Day 18 - Performance Tips and Best Practices

Goal:
Practice vectorization, dtype choices, preallocation, in-place operations, and
memory layout awareness.
"""

from pathlib import Path
from time import perf_counter

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
    section("Avoid Python Loops When Vectorization Fits")
    my_list = list(range(100_000))

    start = perf_counter()
    loop_result = []
    for x in my_list:
        loop_result.append(x**2 + 2 * x + 1)
    loop_seconds = perf_counter() - start

    a = np.array(my_list)
    start = perf_counter()
    vectorized_result = a**2 + 2 * a + 1
    vectorized_seconds = perf_counter() - start

    print("Python loop seconds:", loop_seconds)
    print("NumPy vectorized seconds:", vectorized_seconds)
    print("First 5 loop results:", loop_result[:5])
    show("First 5 vectorized results", vectorized_result[:5])

    section("Choose the Correct dtype")
    float64_values = np.ones(1_000_000, dtype=np.float64)
    float32_values = np.ones(1_000_000, dtype=np.float32)
    print("float64 memory:", float64_values.nbytes, "bytes")
    print("float32 memory:", float32_values.nbytes, "bytes")

    section("Preallocate Output Arrays")
    values = np.arange(10, dtype=float)
    output = np.empty_like(values)
    np.multiply(values, 2, out=output)
    show("values", values)
    show("output after np.multiply(values, 2, out=output)", output)

    section("Use In-place Operations When Appropriate")
    inplace = np.array([1, 2, 3], dtype=float)
    show("before inplace += 10", inplace)
    inplace += 10
    show("after inplace += 10", inplace)

    section("Memory Layout")
    c_order = np.ones((3, 4), order="C")
    f_order = np.ones((3, 4), order="F")
    print("C-order array is C contiguous:", c_order.flags.c_contiguous)
    print("C-order array is F contiguous:", c_order.flags.f_contiguous)
    print("F-order array is C contiguous:", f_order.flags.c_contiguous)
    print("F-order array is F contiguous:", f_order.flags.f_contiguous)

    section("Memory-mapped Files for Large Data")
    temp_dir = Path(__file__).resolve().parent / "generated_data"
    temp_dir.mkdir(exist_ok=True)
    memmap_path = temp_dir / "demo_memmap.dat"

    mapped = np.memmap(memmap_path, dtype="float32", mode="w+", shape=(5,))
    mapped[:] = np.linspace(0, 1, 5)
    mapped.flush()
    show("np.array(mapped)", np.array(mapped))
    del mapped

    try:
        memmap_path.unlink()
    except OSError:
        print("Could not remove temporary memmap file:", memmap_path)

    section("Best Practice Checklist")
    print("- Prefer vectorized array expressions over Python loops.")
    print("- Use @ or np.dot for matrix multiplication.")
    print("- Pick the smallest dtype that correctly stores your data.")
    print("- Use out= or in-place operations to reduce temporary arrays.")
    print("- Use np.memmap for arrays too large to fully load into memory.")


if __name__ == "__main__":
    main()
