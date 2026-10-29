#!/usr/bin/env python3
"""Prepare a Shopify product CSV with reviewed replacements for 原創 copy."""

import argparse
import csv
import datetime
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "Output"
DOWNLOADS_DIR = Path.home() / "Downloads"
EXPECTED_ROWS = 1259
EXPECTED_PRODUCTS = 93
REPLACEMENTS = {
    "指尖原創拉環設計": ("指尖拉環設計", 37),
    "原創 BioXCell 兩階段防手麻搭配Econyl® 海洋再生尼龍": (
        "BioXCell 兩階段防手麻設計，搭配 Econyl® 海洋再生尼龍",
        1,
    ),
    "Lycra® Solar 原創透光均勻曬膚科技": (
        "Lycra® Solar 透光均勻曬膚科技",
        1,
    ),
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None:
            raise ValueError(f"CSV has no header: {path}")
        return reader.fieldnames, list(reader)


def validate_variants(rows: list[dict[str, str]]) -> None:
    seen: set[tuple[str, str, str, str]] = set()
    for row_number, row in enumerate(rows, start=2):
        key = (
            row.get("Handle", ""),
            row.get("Option1 Value", ""),
            row.get("Option2 Value", ""),
            row.get("Option3 Value", ""),
        )
        if key in seen:
            raise ValueError(
                f"Duplicate variant combination at CSV row {row_number}: {key}"
            )
        seen.add(key)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clean reviewed 原創 wording in a Shopify product CSV."
    )
    parser.add_argument(
        "input_csv",
        type=Path,
        help="Current Shopify product CSV export to use as the source",
    )
    args = parser.parse_args()
    input_csv = args.input_csv
    if not input_csv.is_absolute():
        input_csv = ROOT / input_csv

    fieldnames, rows = read_csv(input_csv)
    required_fields = {
        "Handle",
        "Body (HTML)",
        "Option1 Value",
        "Option2 Value",
        "Option3 Value",
    }
    missing_fields = required_fields.difference(fieldnames)
    if missing_fields:
        raise ValueError(f"CSV is missing required fields: {sorted(missing_fields)}")
    if len(rows) != EXPECTED_ROWS:
        raise ValueError(f"Expected {EXPECTED_ROWS} rows, found {len(rows)}")
    product_count = len({row.get("Handle", "") for row in rows if row.get("Handle")})
    if product_count != EXPECTED_PRODUCTS:
        raise ValueError(
            f"Expected {EXPECTED_PRODUCTS} product handles, found {product_count}"
        )

    validate_variants(rows)
    found_counts = {
        phrase: sum((row.get("Body (HTML)") or "").count(phrase) for row in rows)
        for phrase in REPLACEMENTS
    }
    for phrase, (_, expected_count) in REPLACEMENTS.items():
        if found_counts[phrase] != expected_count:
            raise ValueError(
                f"Expected {expected_count} occurrences of {phrase!r}, "
                f"found {found_counts[phrase]}"
            )

    for row in rows:
        body = row.get("Body (HTML)") or ""
        for phrase, (replacement, _) in REPLACEMENTS.items():
            body = body.replace(phrase, replacement)
        row["Body (HTML)"] = body

    if any("原創" in (row.get("Body (HTML)") or "") for row in rows):
        raise ValueError("Unreviewed 原創 wording remains in product descriptions")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    filename = f"CHIBA_Shopify_Full_Products_Cleaned_{timestamp}.csv"
    output_path = OUTPUT_DIR / filename
    downloads_path = DOWNLOADS_DIR / filename
    if output_path.exists() or downloads_path.exists():
        raise FileExistsError(f"Refusing to overwrite an existing export: {filename}")

    with output_path.open("w", encoding="utf-8-sig", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    shutil.copy2(output_path, downloads_path)

    exported_headers, exported_rows = read_csv(output_path)
    if exported_headers != fieldnames or len(exported_rows) != EXPECTED_ROWS:
        raise ValueError("Exported CSV failed the structure re-read check")
    validate_variants(exported_rows)
    if any("原創" in value for row in exported_rows for value in row.values() if value):
        raise ValueError("Exported CSV still contains 原創")
    if output_path.read_bytes() != downloads_path.read_bytes():
        raise ValueError("Downloads copy does not match the project export")

    print(f"Prepared {output_path}")
    print(f"Copied   {downloads_path}")
    print(f"Verified {len(exported_rows)} rows, {len(exported_headers)} columns,")
    print(f"         0 原創 occurrences in Body (HTML); 0 duplicate variant keys")
    print("Replacements:")
    for phrase, (replacement, count) in REPLACEMENTS.items():
        print(f"  {count}x {phrase} -> {replacement}")


if __name__ == "__main__":
    main()
