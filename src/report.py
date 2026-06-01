import csv
from pathlib import Path


def save_report(results: list[dict], report_file: Path) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)

    with report_file.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["filename", "category", "status", "reason"],
        )

        writer.writeheader()
        writer.writerows(results)
