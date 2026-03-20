# sample1.py
# Print a simple dashboard table to the console.

from __future__ import annotations


def build_dataset() -> list[dict[str, float]]:
    return [
        {"item": "A", "value": 10.0, "score": 0.75},
        {"item": "B", "value": 22.5, "score": 0.52},
        {"item": "C", "value": 15.1, "score": 0.95},
        {"item": "D", "value": 7.3, "score": 0.33},
    ]


def print_table(rows: list[dict[str, float]]) -> None:
    headers = list(rows[0].keys())
    col_widths = {h: max(len(h), max(len(str(r[h])) for r in rows)) for h in headers}

    def print_row(row: dict[str, float]) -> None:
        print(" | ".join(str(row[h]).ljust(col_widths[h]) for h in headers))

    print_row({h: h for h in headers})
    print("-+-".join("-" * col_widths[h] for h in headers))
    for r in rows:
        print_row(r)


def main() -> None:
    data = build_dataset()
    print("Simple Data Dashboard")
    print_table(data)


if __name__ == "__main__":
    main()
