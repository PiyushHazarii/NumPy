"""
Day 14 - File I/O with NumPy

Goal:
Save and load arrays using .npy, .npz, compressed .npz, text, and CSV formats.
"""

from pathlib import Path

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
    output_dir = Path(__file__).resolve().parent / "generated_data"
    output_dir.mkdir(exist_ok=True)

    arr = np.arange(12).reshape(3, 4)
    arr1 = np.array([10, 20, 30])
    arr2 = np.array([[1.5, 2.5], [3.5, 4.5]])

    section("Save and Load One Array: .npy")
    npy_path = output_dir / "data.npy"
    np.save(npy_path, arr)
    loaded = np.load(npy_path)
    show("original arr", arr)
    show("loaded from data.npy", loaded)

    section("Save and Load Multiple Arrays: .npz")
    npz_path = output_dir / "data.npz"
    np.savez(npz_path, x=arr1, y=arr2)
    with np.load(npz_path) as data:
        show("data['x']", data["x"])
        show("data['y']", data["y"])

    section("Compressed .npz")
    compressed_path = output_dir / "data_compressed.npz"
    np.savez_compressed(compressed_path, x=arr, y=arr2)
    print("Compressed file created:", compressed_path)

    section("Text / CSV")
    csv_path = output_dir / "data.csv"
    np.savetxt(csv_path, arr2, delimiter=",", fmt="%.4f")
    loaded_csv = np.loadtxt(csv_path, delimiter=",")
    show("loaded CSV with np.loadtxt", loaded_csv)

    section("genfromtxt for Missing Values")
    missing_csv_path = output_dir / "missing_values.csv"
    missing_csv_path.write_text("1,2,3\n4,,6\n7,8,\n", encoding="utf-8")
    loaded_missing = np.genfromtxt(missing_csv_path, delimiter=",", filling_values=0)
    show("np.genfromtxt(..., filling_values=0)", loaded_missing)

    print("\nFiles were written to:")
    print(output_dir)


if __name__ == "__main__":
    main()
