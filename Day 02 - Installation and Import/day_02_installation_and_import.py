"""
Day 02 - Installation and Import

Goal:
Learn the standard NumPy import style and basic environment checks.
"""

try:
    import numpy as np
except ImportError as exc:
    raise SystemExit(
        "NumPy is not installed. Install it with: pip install numpy"
    ) from exc


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def show(label, value):
    print(f"\n{label}:")
    print(value)


def main():
    section("Standard Import")
    print("The standard alias is:")
    print("import numpy as np")
    print("Use this alias because almost every NumPy codebase uses np.")

    section("Check NumPy Version")
    print("NumPy version:", np.__version__)

    section("Your First Arrays")
    one_dimensional = np.array([10, 20, 30])
    two_dimensional = np.array([[1, 2, 3], [4, 5, 6]])

    show("1-D array", one_dimensional)
    show("2-D array", two_dimensional)

    section("Quick Environment Smoke Test")
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4), dtype=int)
    identity = np.eye(4)

    show("np.zeros((3, 3))", zeros)
    show("np.ones((2, 4), dtype=int)", ones)
    show("np.eye(4)", identity)

    section("Tiny Exercise")
    print("Create a NumPy array from your own list and print its shape.")
    my_scores = np.array([45, 62, 88, 91])
    show("my_scores", my_scores)
    print("shape:", my_scores.shape)


if __name__ == "__main__":
    main()
