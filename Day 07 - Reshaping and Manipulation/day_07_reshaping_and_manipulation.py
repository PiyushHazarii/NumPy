"""
Day 07 - Array Reshaping and Manipulation

Goal:
Use reshape, flatten, ravel, transpose, dimension changes, stacking, and
splitting.
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
    section("reshape")
    a = np.arange(12)
    b = a.reshape(3, 4)
    c = a.reshape(2, 2, 3)
    d = a.reshape(-1, 4)

    show("a = np.arange(12)", a)
    show("a.reshape(3, 4)", b)
    show("a.reshape(2, 2, 3)", c)
    show("a.reshape(-1, 4) - infer rows", d)

    section("flatten vs ravel")
    matrix = np.arange(6).reshape(2, 3)
    flattened = matrix.flatten()
    raveled = matrix.ravel()

    show("matrix", matrix)
    show("matrix.flatten() - copy", flattened)
    show("matrix.ravel() - view when possible", raveled)

    raveled[0] = 999
    show("matrix after raveled[0] = 999", matrix)
    print("flattened is independent:", flattened)

    print("np.shares_memory(matrix, raveled):", np.shares_memory(matrix, raveled))
    print("np.shares_memory(matrix, flattened):", np.shares_memory(matrix, flattened))

    section("transpose")
    show("b", b)
    show("b.T", b.T) # this and the below (b,(1,0)) are equivalent.
    show("np.transpose(b, (1, 0))", np.transpose(b, (1, 0)))

    section("Adding and Removing Dimensions")
    vector = np.arange(5)
    row_vector = vector[np.newaxis, :]
    column_vector = vector[:, np.newaxis]
    expanded = np.expand_dims(vector, axis=0)
    squeezed = np.squeeze(np.zeros((1, 3, 1)))

    show("vector", vector)
    show("vector[np.newaxis, :]", row_vector)
    show("vector[:, np.newaxis]", column_vector)
    show("np.expand_dims(vector, axis=0)", expanded)
    show("np.squeeze(np.zeros((1, 3, 1)))", squeezed)

    section("Concatenation and Stacking")
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])

    show("arr1", arr1)
    show("arr2", arr2)

    #In NumPy, both concatenation and stacking always create a copy.
    show("np.concatenate([arr1, arr2], axis=0)", np.concatenate([arr1, arr2], axis=0))
    show("np.concatenate([arr1, arr2], axis=1)", np.concatenate([arr1, arr2], axis=1))
    show("np.vstack([arr1, arr2])", np.vstack([arr1, arr2]))
    show("np.hstack([arr1, arr2])", np.hstack([arr1, arr2]))

    section("Splitting")
    long_array = np.arange(12)
    grid = np.arange(16).reshape(4, 4)

    show("np.split(long_array, 3)", np.split(long_array, 3))
    show("grid", grid)
    show("np.vsplit(grid, 2)", np.vsplit(grid, 2))
    show("np.hsplit(grid, 2)", np.hsplit(grid, 2))


if __name__ == "__main__":
    main()
