#!/usr/bin/env python3
"""Refresh assets/julia-stats.json from Julia's official package-request telemetry.

Source: https://julialang-logs.s3.amazonaws.com/public_outputs/current/
        (package_requests.csv.gz, aggregated per package UUID)
"""

from __future__ import annotations

import csv
import gzip
import io
import json
import urllib.request
from datetime import date
from pathlib import Path

DATASET_URL = (
    "https://julialang-logs.s3.amazonaws.com/public_outputs/current/package_requests.csv.gz"
)
GLENN_UUID = "d531567c-0c1c-43c6-9163-287e3bec9c15"
OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "julia-stats.json"


def fetch_glenn_rows(url: str = DATASET_URL) -> list[dict[str, str]]:
    with urllib.request.urlopen(url, timeout=180) as response:
        payload = gzip.decompress(response.read())
    reader = csv.DictReader(io.StringIO(payload.decode("utf-8")))
    return [row for row in reader if row["package_uuid"] == GLENN_UUID]


def build_badge(rows: list[dict[str, str]]) -> dict[str, object]:
    requests = sum(int(row["request_count"] or 0) for row in rows)
    starts = [row["date_min"] for row in rows if row["date_min"]]
    ends = [row["date_max"] for row in rows if row["date_max"]]
    window = "n/a"
    if starts and ends:
        first, last = min(starts), max(ends)
        days = (date.fromisoformat(last) - date.fromisoformat(first)).days + 1
        window = f"{days} d"
    return {
        "schemaVersion": 1,
        "label": "Glenn.jl requests",
        "message": f"{requests:,} / {window}",
        "color": "9558B2",
    }


def main() -> None:
    badge = build_badge(fetch_glenn_rows())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(badge, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.name}: {badge['message']}")


if __name__ == "__main__":
    main()
