"""
Day 16 - String Operations (numpy.char)

Goal:
Use NumPy's vectorized string helper functions.
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
    section("Basic String Array")
    s = np.array(["hello", "world", "numpy"])
    show("s", s)

    section("Case Conversion")
    show("np.char.upper(s)", np.char.upper(s))
    show("np.char.lower(s)", np.char.lower(s))
    show("np.char.capitalize(s)", np.char.capitalize(s))

    section("Strip and Replace")
    messy = np.array(["  apple  ", " banana", "cherry  "])
    show("messy", messy)
    show("np.char.strip(messy)", np.char.strip(messy))
    show("np.char.replace(s, 'o', '0')", np.char.replace(s, "o", "0"))

    section("Split, Join, Find, Add")
    phrases = np.array(["data science", "machine learning", "numpy arrays"])
    show("phrases", phrases)
    show("np.char.split(phrases)", np.char.split(phrases))
    show("np.char.join('-', s)", np.char.join("-", s))
    show("np.char.find(s, 'l')", np.char.find(s, "l"))
    show("np.char.add(s, '!')", np.char.add(s, "!"))

    section("Mini Practice")
    names = np.array([" piyush ", " numpy ", " python "])
    cleaned = np.char.capitalize(np.char.strip(names))
    labels = np.char.add("Student: ", cleaned)
    show("cleaned names", cleaned)
    show("labels", labels)


if __name__ == "__main__":
    main()
