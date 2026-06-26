"""
Day 09 - Statistical Functions

Goal:
Calculate mean, median, spread, percentiles, correlation, covariance, and
histograms.
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
    section("Basic Statistics")
    a = np.array([2, 4, 6, 8, 10])
    show("a", a)

    print("np.mean(a):", np.mean(a))
    print("np.median(a):", np.median(a))
    print("np.std(a):", np.std(a))
    print("np.var(a):", np.var(a))
    print("np.min(a):", np.min(a))
    print("np.max(a):", np.max(a))
    print("np.ptp(a):", np.ptp(a))
    print("np.argmin(a):", np.argmin(a))
    print("np.argmax(a):", np.argmax(a))

    section("Percentiles and Quantiles")
    print("np.percentile(a, 25):", np.percentile(a, 25))
    print("np.percentile(a, 75):", np.percentile(a, 75))
    print("np.quantile(a, 0.5):", np.quantile(a, 0.5))

    section("Axis-wise Statistics")
    marks = np.array(
        [
            [70, 80, 90],
            [60, 75, 85],
            [95, 88, 92],
        ]
    )
    show("marks", marks)
    show("subject-wise mean, axis=0", np.mean(marks, axis=0))
    show("student-wise mean, axis=1", np.mean(marks, axis=1))
    show("subject-wise max, axis=0", np.max(marks, axis=0))

    section("Correlation and Covariance")
    study_hours = np.array([1, 2, 3, 4, 5])
    scores = np.array([45, 55, 65, 75, 85])
    show("study_hours", study_hours)
    show("scores", scores)
    show("np.corrcoef(study_hours, scores)", np.corrcoef(study_hours, scores))
    show("np.cov(study_hours, scores)", np.cov(study_hours, scores))

    section("Histogram")
    data = np.array([1, 1, 2, 2, 2, 3, 4, 5, 5])
    counts, bin_edges = np.histogram(data, bins=5)
    show("data", data)
    show("histogram counts", counts)
    show("histogram bin edges", bin_edges)


if __name__ == "__main__":
    main()
