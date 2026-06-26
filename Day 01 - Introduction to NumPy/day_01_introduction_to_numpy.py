"""
Day 01 - Introduction to NumPy

Goal:
Understand why NumPy exists and how vectorized array operations differ from
normal Python list loops.
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
    section("What is NumPy?")
    print("NumPy means Numerical Python.")
    print("It gives Python fast N-dimensional arrays and vectorized math.")
    print("Libraries like pandas, SciPy, Matplotlib, and scikit-learn build on it.")

    section("Python List vs NumPy Array")
    python_list = [1, 2, 3, 4, 5]
    numpy_array = np.array([1, 2, 3, 4, 5])

    show("Python list", python_list)
    show("NumPy array", numpy_array)

    print("\nAdding 10 to every value:")
    list_result = [value + 10 for value in python_list]
    array_result = numpy_array + 10
    show("List result using a loop/list-comprehension", list_result)
    show("NumPy result using vectorization", array_result)

    section("Element-wise Math")
    marks = np.array([70, 85, 90, 60])
    bonus = np.array([5, 3, 4, 10])
    final_marks = marks + bonus

    show("Original marks", marks)
    show("Bonus marks", bonus)
    show("Final marks", final_marks)

    section("Memory and dtype Idea")
    small = np.array([1, 2, 3], dtype=np.int8)
    normal = np.array([1, 2, 3], dtype=np.int64)

    show("Small int8 array", small)
    print("int8 bytes per element:", small.itemsize)
    print("int64 bytes per element:", normal.itemsize)
    print("Choosing a good dtype saves memory.")

    section("Mini Practice")
    prices = np.array([100, 250, 500, 1000])
    discount_percent = 10
    discounted_prices = prices - (prices * discount_percent / 100)

    show("Prices", prices)
    show("Prices after 10 percent discount", discounted_prices)


if __name__ == "__main__":
    main()
