"""
Day 20 - Quick Reference Cheat Sheet

Goal:
Run one compact file that touches the main NumPy tools from the full notes.
"""

from pathlib import Path

try:
    import numpy as np
    import numpy.linalg as la
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
    section("Creation")
    a = np.array([1, 2, 3])
    matrix = np.arange(1, 10).reshape(3, 3)
    show("np.array([1, 2, 3])", a)
    show("np.zeros((2, 3))", np.zeros((2, 3)))
    show("np.ones((2, 3))", np.ones((2, 3)))
    show("np.arange(0, 10, 2)", np.arange(0, 10, 2))
    show("np.linspace(0, 1, 5)", np.linspace(0, 1, 5))
    show("np.eye(3)", np.eye(3))

    section("Shape")
    show("matrix", matrix)
    print("matrix.shape:", matrix.shape)
    print("matrix.ndim:", matrix.ndim)
    print("matrix.size:", matrix.size)
    print("matrix.dtype:", matrix.dtype)
    show("matrix.flatten()", matrix.flatten())
    show("matrix.T", matrix.T)

    section("Indexing")
    show("a[1:]", a[1:])
    print("matrix[1, 2]:", matrix[1, 2])
    show("matrix[:, 0]", matrix[:, 0])
    show("matrix[matrix > 4]", matrix[matrix > 4])
    show("np.where(matrix > 5, matrix, 0)", np.where(matrix > 5, matrix, 0))

    section("Math")
    show("a + 10", a + 10)
    show("a * a", a * a)
    show("np.sqrt(a)", np.sqrt(a))
    show("np.clip(matrix, 3, 7)", np.clip(matrix, 3, 7))

    section("Stats")
    print("np.mean(matrix):", np.mean(matrix))
    print("np.median(matrix):", np.median(matrix))
    print("np.std(matrix):", np.std(matrix))
    print("np.min(matrix):", np.min(matrix))
    print("np.max(matrix):", np.max(matrix))
    print("np.argmax(matrix):", np.argmax(matrix))

    section("Linear Algebra")
    A = np.array([[1, 2], [3, 4]], dtype=float)
    b = np.array([1, 2], dtype=float)
    show("A", A)
    show("A @ A", A @ A)
    print("la.det(A):", la.det(A))
    show("la.inv(A)", la.inv(A))
    show("la.solve(A, b)", la.solve(A, b))

    section("Random")
    rng = np.random.default_rng(seed=42)
    show("rng.random(3)", rng.random(3))
    show("rng.integers(0, 10, size=5)", rng.integers(0, 10, size=5))
    show("rng.normal(0, 1, size=5)", rng.normal(0, 1, size=5))

    section("Sort and Search")
    values = np.array([3, 1, 4, 1, 5])
    show("values", values)
    show("np.sort(values)", np.sort(values))
    show("np.argsort(values)", np.argsort(values))
    show("np.unique(values, return_counts=True)", np.unique(values, return_counts=True))
    print("np.searchsorted(np.sort(values), 4):", np.searchsorted(np.sort(values), 4))

    section("File I/O")
    output_dir = Path(__file__).resolve().parent / "generated_data"
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / "quick_array.npy"
    np.save(file_path, matrix)
    loaded = np.load(file_path)
    show("loaded quick_array.npy", loaded)

    section("Broadcasting")
    col = np.arange(3).reshape(3, 1)
    row = np.arange(3)
    show("col", col)
    show("row", row)
    show("col + row", col + row)

    print("\nYou have covered the full PDF outline in runnable NumPy code.")


if __name__ == "__main__":
    main()
