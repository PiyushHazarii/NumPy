# NumPy Day-wise Practice Course

A structured 20-day NumPy learning project based on `NumPy_Complete_Notes.pdf`.

This repository turns the notes into practical, runnable Python scripts. Each day focuses on one NumPy topic, prints clear examples, and is designed so you can edit values and immediately see how NumPy behaves.

## What You Will Learn

By completing these lessons, you will understand how to:

- Create and inspect NumPy arrays.
- Work with `ndarray`, `dtype`, shape, dimensions, and memory usage.
- Use indexing, slicing, boolean masks, and fancy indexing.
- Reshape, stack, split, flatten, and transpose arrays.
- Perform vectorized mathematical and statistical operations.
- Use broadcasting to combine arrays with different shapes.
- Apply NumPy linear algebra, random number generation, file I/O, sorting, strings, and datetime tools.
- Write faster array-based code instead of slow Python loops.

## Project Structure

Each folder contains one standalone Python file for that day.

```text
NumPy/
|-- Phase1.py
|-- README.md
|-- Day 01 - Introduction to NumPy/
|   `-- day_01_introduction_to_numpy.py
|-- Day 02 - Installation and Import/
|   `-- day_02_installation_and_import.py
|-- ...
`-- Day 20 - Quick Reference Cheat Sheet/
    `-- day_20_quick_reference_cheat_sheet.py
```

## Requirements

- Python 3.9 or newer
- NumPy
- A code editor such as VS Code, PyCharm, or any editor you prefer

Install NumPy:

```powershell
pip install numpy
```

Check your NumPy installation:

```powershell
python -c "import numpy as np; print(np.__version__)"
```

If `python` is not recognized, choose the correct Python interpreter inside your IDE or install Python from the official Python website.

## How to Run a Lesson

Open a terminal in this project folder:

```powershell
cd "C:\Users\Asus\Music\NumPy"
```

Run any day file like this:

```powershell
python "Day 01 - Introduction to NumPy\day_01_introduction_to_numpy.py"
```

Example for Day 10:

```powershell
python "Day 10 - Broadcasting\day_10_broadcasting.py"
```

You can also run the active file directly from your IDE.

## Recommended Study Method

1. Open the day folder.
2. Read the script from top to bottom.
3. Run the file once without changing anything.
4. Change the sample arrays and run it again.
5. Add one small experiment at the bottom of the file.
6. Move to the next day only after the output makes sense.

The best way to learn NumPy is not just to read the code, but to break it gently and see what NumPy tells you.

## Day-wise Syllabus

| Day | Topic | Main Practice |
| --- | --- | --- |
| 01 | Introduction to NumPy | Why NumPy is used, arrays vs lists, vectorized operations |
| 02 | Installation and Import | `import numpy as np`, version check, first arrays |
| 03 | NumPy Arrays ndarray | 1-D, 2-D, 3-D arrays, `dtype`, type casting |
| 04 | Array Creation Methods | `zeros`, `ones`, `full`, `empty`, `eye`, `arange`, `linspace` |
| 05 | Array Attributes | `ndim`, `shape`, `size`, `dtype`, `itemsize`, `nbytes`, transpose |
| 06 | Indexing and Slicing | 1-D and 2-D indexing, slices, views vs copies |
| 07 | Reshaping and Manipulation | `reshape`, `flatten`, `ravel`, stacking, splitting |
| 08 | Mathematical Operations | Element-wise arithmetic, ufuncs, aggregation functions |
| 09 | Statistical Functions | Mean, median, standard deviation, variance, percentile, histogram |
| 10 | Broadcasting | Broadcasting rules, scalar-array math, row and column operations |
| 11 | Boolean and Fancy Indexing | Masks, `np.where`, selecting with index arrays, `np.ix_` |
| 12 | Linear Algebra | Matrix multiplication, determinant, inverse, solve, SVD |
| 13 | Random Module | `default_rng`, random integers, distributions, shuffle, permutation |
| 14 | File I/O with NumPy | Save and load `.npy`, `.npz`, compressed files, CSV/text files |
| 15 | Sorting and Searching | `sort`, `argsort`, `where`, `searchsorted`, `unique` |
| 16 | String Operations | `numpy.char` functions for case, replace, split, join, find |
| 17 | Datetime in NumPy | `datetime64`, `timedelta64`, date arrays, date arithmetic |
| 18 | Performance Tips | Vectorization, dtype memory, preallocation, in-place operations |
| 19 | NumPy vs Python Lists | Speed, memory, math behavior, dimensions, broadcasting |
| 20 | Quick Reference Cheat Sheet | Compact revision of the most important NumPy commands |

## Generated Files

Some lessons create temporary practice output:

- Day 14 creates files inside `Day 14 - File IO with NumPy/generated_data/`.
- Day 18 may create a temporary memory-mapped file while running.
- Day 20 creates `quick_array.npy` inside its own `generated_data/` folder.

These files are only for practice and can be deleted safely.

## Common Problems

### `ModuleNotFoundError: No module named 'numpy'`

Install NumPy:

```powershell
pip install numpy
```

If you use a virtual environment, activate it first, then install NumPy.

### `python is not recognized`

Python is not available from your terminal PATH. Use one of these options:

- Run the file from your IDE using the selected Python interpreter.
- Install Python and enable the "Add Python to PATH" option.
- Try `py` instead of `python` if the Python launcher is available.

### File paths with spaces are not working

Wrap the path in quotes:

```powershell
python "Day 03 - NumPy Arrays ndarray\day_03_numpy_arrays_ndarray.py"
```

## Learning Tip

After each lesson, create a small example using your own data. For example, use marks, prices, temperatures, expenses, or product quantities. NumPy becomes much easier when the arrays represent something familiar.

