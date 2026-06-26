"""
Day 12 - Linear Algebra

Goal:
Use matrix multiplication, determinants, inverses, decompositions, and solvers.
"""

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
    A = np.array([[1, 2], [3, 4]], dtype=float)
    B = np.array([[5, 6], [7, 8]], dtype=float)

    section("Matrices")
    show("A", A)
    show("B", B)

    section("Matrix Multiplication")
    show("A @ B", A @ B)
    show("np.dot(A, B)", np.dot(A, B))
    show("np.matmul(A, B)", np.matmul(A, B))
    print("Use @ in modern Python code because it clearly means matrix multiplication.")

    section("Key Operations")
    print("la.det(A):", la.det(A))
    show("la.inv(A)", la.inv(A))
    print("la.matrix_rank(A):", la.matrix_rank(A))
    print("np.trace(A):", np.trace(A))
    print("la.norm(A):", la.norm(A))
    print("la.norm(A, ord=1):", la.norm(A, ord=1))

    section("Eigenvalues and Eigenvectors")
    values, vectors = la.eig(A)
    show("eigenvalues", values)
    show("eigenvectors", vectors)

    section("Singular Value Decomposition")
    U, S, Vt = la.svd(A)
    show("U", U)
    show("S", S)
    show("Vt", Vt)

    section("Solve Ax = b")
    b = np.array([1, 2], dtype=float)
    x = la.solve(A, b)
    show("b", b)
    show("x = la.solve(A, b)", x)
    show("A @ x - should equal b", A @ x)

    section("Least Squares")
    X = np.array(
        [
            [1, 1],
            [1, 2],
            [1, 3],
        ],
        dtype=float,
    )
    y = np.array([1, 2, 2], dtype=float)
    coefficients, residuals, rank, singular_values = la.lstsq(X, y, rcond=None)

    show("X", X)
    show("y", y)
    show("least-squares coefficients", coefficients)
    show("residuals", residuals)
    print("rank:", rank)
    show("singular values", singular_values)


if __name__ == "__main__":
    main()
