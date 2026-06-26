"""
Day 13 - Random Module (numpy.random)

Goal:
Generate reproducible random numbers with the modern default_rng API and
recognize older random functions.
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
    section("Modern API: default_rng")
    rng = np.random.default_rng(seed=42)

    show("rng.random((3, 3))", rng.random((3, 3)))
    show("rng.integers(0, 10, size=5)", rng.integers(0, 10, size=5))
    show("rng.normal(loc=0, scale=1, size=(2, 3))", rng.normal(loc=0, scale=1, size=(2, 3)))
    show("rng.uniform(1, 10, size=5)", rng.uniform(1, 10, size=5))
    show("rng.choice([1, 2, 3, 4, 5], size=3)", rng.choice([1, 2, 3, 4, 5], size=3))

    section("shuffle vs permutation")
    arr = np.arange(10)
    shuffled_in_place = arr.copy()
    rng.shuffle(shuffled_in_place)
    permutation_copy = rng.permutation(arr)

    show("arr", arr)
    show("rng.shuffle(shuffled_in_place) changes the array", shuffled_in_place)
    show("rng.permutation(arr) returns a shuffled copy", permutation_copy)
    show("arr is still unchanged", arr)

    section("Reproducibility")
    rng_a = np.random.default_rng(seed=7)
    rng_b = np.random.default_rng(seed=7)
    show("rng_a.integers(0, 100, 5)", rng_a.integers(0, 100, 5))
    show("rng_b.integers(0, 100, 5)", rng_b.integers(0, 100, 5))
    print("Same seed means the same random sequence.")

    section("Legacy API")
    np.random.seed(0)
    show("np.random.rand(3, 3)", np.random.rand(3, 3))
    show("np.random.randn(3, 3)", np.random.randn(3, 3))
    show("np.random.randint(0, 10, 5)", np.random.randint(0, 10, 5))
    show("np.random.choice(arr, 5)", np.random.choice(arr, 5))
    show("np.random.binomial(n=10, p=0.5, size=5)", np.random.binomial(n=10, p=0.5, size=5))
    show("np.random.poisson(lam=3, size=5)", np.random.poisson(lam=3, size=5))
    show("np.random.exponential(scale=1.0, size=5)", np.random.exponential(scale=1.0, size=5))

    print("\nUse default_rng() in new code.")


if __name__ == "__main__":
    main()
