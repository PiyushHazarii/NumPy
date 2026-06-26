"""
Day 17 - Datetime in NumPy

Goal:
Use datetime64 and timedelta64 for date arrays and date arithmetic.
"""

import datetime

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
    section("datetime64 Values")
    date_only = np.datetime64("2025-01-15")
    date_time = np.datetime64("2025-01-15T10:30:00")

    show("np.datetime64('2025-01-15')", date_only)
    show("np.datetime64('2025-01-15T10:30:00')", date_time)

    section("Arrays of Dates")
    months = np.arange("2025-01", "2025-07", dtype="datetime64[M]")
    days = np.arange("2025-01-01", "2025-01-08", dtype="datetime64[D]")

    show("months from Jan to Jun 2025", months)
    show("first week of Jan 2025", days)

    section("timedelta64 Arithmetic")
    show("date_only + np.timedelta64(7, 'D')", date_only + np.timedelta64(7, "D"))
    show("date_only - np.datetime64('2025-01-01')", date_only - np.datetime64("2025-01-01"))
    show("days + np.timedelta64(2, 'D')", days + np.timedelta64(2, "D"))

    section("Current Date and Time")
    show("np.datetime64('today')", np.datetime64("today"))
    show("np.datetime64('now')", np.datetime64("now"))
    print("These two outputs change depending on when you run the file.")

    section("From Python datetime")
    python_date = datetime.date(2025, 1, 15)
    python_datetime = datetime.datetime(2025, 1, 15, 10, 30)

    show("python date", python_date)
    show("np.datetime64(python_date)", np.datetime64(python_date))
    show("np.datetime64(python_datetime)", np.datetime64(python_datetime))

    section("Mini Practice")
    start = np.datetime64("2025-06-01")
    study_days = start + np.arange(7).astype("timedelta64[D]")
    show("7-day NumPy study plan dates", study_days)


if __name__ == "__main__":
    main()
