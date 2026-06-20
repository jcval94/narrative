from __future__ import annotations

import argparse
import csv
import random
from datetime import date, timedelta
from pathlib import Path

import yaml


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def movements_incentives(seed: int, n: int) -> list[dict[str, object]]:
    rng = random.Random(seed)
    rows: list[dict[str, object]] = []
    start = date(2025, 1, 1)
    for i in range(n):
        period = "after_alert" if i >= n * 0.62 else "before_alert"
        if period == "before_alert" and rng.random() < 0.18:
            amount = rng.uniform(-2.04, -0.71)
            source_type = "employee_account"
        elif period == "after_alert" and rng.random() < 0.18:
            amount = rng.uniform(0.72, 2.15)
            source_type = "external_bank"
        else:
            amount = rng.triangular(-10, 10, 0)
            source_type = rng.choice(["customer_cash", "customer_transfer", "employee_account"])
        rows.append(
            {
                "case_id": f"MI-{i + 1:04d}",
                "period": period,
                "open_date": (start + timedelta(days=rng.randint(0, 210))).isoformat(),
                "days_since_open": rng.randint(0, 60),
                "movement_amount": round(amount, 2),
                "source_type": source_type,
                "activated": 1,
            }
        )
    return rows


def cancellations_window(seed: int, n: int) -> list[dict[str, object]]:
    rng = random.Random(seed)
    reasons = ["Economía Personal", "Mala Venta", "Precio", "Cambio de Producto", "Servicio"]
    rows: list[dict[str, object]] = []
    for i in range(n):
        reason = rng.choices(reasons, weights=[24, 22, 18, 16, 20], k=1)[0]
        if reason in {"Economía Personal", "Mala Venta"}:
            month_since_open = max(1, min(24, int(rng.gauss(10, 3))))
        else:
            month_since_open = max(1, min(24, int(rng.gauss(4, 2))))
        rows.append(
            {
                "case_id": f"CA-{i + 1:04d}",
                "month_since_open": month_since_open,
                "cancel_reason": reason,
                "visible_in_tool": int(month_since_open <= 3),
                "included_in_6m_cut": int(month_since_open <= 6),
            }
        )
    return rows


def kpi_definition_shift(seed: int, n: int) -> list[dict[str, object]]:
    rng = random.Random(seed)
    rows: list[dict[str, object]] = []
    start = date(2025, 1, 1)
    for i in range(n):
        month_index = i % 12
        after_change = month_index >= 6
        complex_case = rng.random() < (0.34 if not after_change else 0.08)
        base_resolution = 0.82 if not complex_case else 0.48
        resolved_sla = int(rng.random() < base_resolution)
        rows.append(
            {
                "case_id": f"KPI-{i + 1:04d}",
                "month": (start + timedelta(days=30 * month_index)).strftime("%Y-%m"),
                "definition_version": "v2_excludes_complex" if after_change else "v1_all_cases",
                "complex_case": int(complex_case),
                "included_in_kpi": int((not after_change) or (not complex_case)),
                "resolved_sla": resolved_sla,
            }
        )
    return rows


SCENARIOS = {
    "movements_incentives": movements_incentives,
    "cancellations_window": cancellations_window,
    "kpi_definition_shift": kpi_definition_shift,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate synthetic data for narrative examples.")
    parser.add_argument("spec_path", type=Path)
    parser.add_argument("output_path", type=Path)
    args = parser.parse_args()

    spec = yaml.safe_load(args.spec_path.read_text(encoding="utf-8"))
    scenario = spec.get("scenario")
    seed = int(spec.get("seed", 7))
    rows_count = int(spec.get("rows", 300))

    if scenario not in SCENARIOS:
        valid = ", ".join(sorted(SCENARIOS))
        raise SystemExit(f"Unknown scenario '{scenario}'. Valid scenarios: {valid}")

    rows = SCENARIOS[scenario](seed, rows_count)
    write_csv(args.output_path, rows)
    print(f"Wrote {len(rows)} rows to {args.output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

