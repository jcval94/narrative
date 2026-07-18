#!/usr/bin/env python3
"""Discover canonical narrative cases without a hard-coded registry."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


STORY_BLOCK = re.compile(r"<!--\s*story\s*(.*?)-->", re.DOTALL | re.IGNORECASE)
FIELD = re.compile(r"^([a-z_]+):\s*(.*?)\s*$")
CASE_ID = re.compile(r"^(\d+)_")


def default_repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def parse_story_metadata(text: str) -> dict[str, str]:
    match = STORY_BLOCK.search(text)
    if not match:
        return {}
    metadata: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        field = FIELD.match(raw_line.strip())
        if field:
            metadata[field.group(1)] = field.group(2)
    return metadata


def discover_cases(repo_root: Path) -> list[dict[str, Any]]:
    cases_dir = repo_root / "examples" / "cases"
    data_dir = repo_root / "examples" / "data_specs"
    visual_dir = repo_root / "examples" / "visual_specs"
    html_dir = repo_root / "examples" / "html"
    cases: list[dict[str, Any]] = []

    for case_path in sorted(cases_dir.glob("*.md")):
        text = case_path.read_text(encoding="utf-8")
        metadata = parse_story_metadata(text)
        filename_id = CASE_ID.match(case_path.name)
        case_id = metadata.get("case_id") or (filename_id.group(1) if filename_id else "")
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        stem = case_path.stem
        companions = {
            "data_spec": data_dir / f"{stem}.yml",
            "visual_spec": visual_dir / f"{stem}.yml",
            "html": html_dir / f"{stem}.html",
        }
        errors: list[str] = []
        if not case_id:
            errors.append("missing numeric case id")
        if metadata.get("case_id") and filename_id and metadata["case_id"] != filename_id.group(1):
            errors.append("story case_id does not match filename")
        if not metadata:
            errors.append("missing story metadata block")
        for field in ("concept", "situation", "bad_logic", "data_turn", "decision", "rule"):
            if not metadata.get(field):
                errors.append(f"missing story field: {field}")
        for kind, path in companions.items():
            if not path.exists():
                errors.append(f"missing {kind}: {path.relative_to(repo_root)}")

        cases.append(
            {
                "case_id": case_id,
                "title": title_match.group(1).strip() if title_match else case_path.stem,
                "path": case_path.relative_to(repo_root).as_posix(),
                "concept": metadata.get("concept", ""),
                "situation": metadata.get("situation", ""),
                "bad_logic": metadata.get("bad_logic", ""),
                "data_turn": metadata.get("data_turn", ""),
                "decision": metadata.get("decision", ""),
                "punchline": metadata.get("punchline", ""),
                "rule": metadata.get("rule", ""),
                "synthetic_data": metadata.get("synthetic_data", "").lower() == "true",
                "companions": {
                    key: value.relative_to(repo_root).as_posix() for key, value in companions.items()
                },
                "valid": not errors,
                "errors": errors,
            }
        )

    cases_by_id: dict[str, list[dict[str, Any]]] = {}
    for case in cases:
        cases_by_id.setdefault(str(case["case_id"]), []).append(case)
    for case_id, duplicates in cases_by_id.items():
        if case_id and len(duplicates) > 1:
            for case in duplicates:
                case["errors"].append(f"duplicate case id: {case_id}")
                case["valid"] = False

    def sort_key(case: dict[str, Any]) -> tuple[int, str]:
        raw_id = str(case["case_id"])
        return (int(raw_id) if raw_id.isdigit() else sys.maxsize, case["path"])

    return sorted(cases, key=sort_key)


def next_case_id(cases: list[dict[str, Any]]) -> str:
    numeric = [int(str(case["case_id"])) for case in cases if str(case["case_id"]).isdigit()]
    next_id = max(numeric, default=0) + 1
    width = max(2, max((len(str(case["case_id"])) for case in cases), default=2))
    return str(next_id).zfill(width)


def build_catalog(repo_root: Path) -> dict[str, Any]:
    cases = discover_cases(repo_root)
    return {
        "repo_root": str(repo_root.resolve()),
        "case_count": len(cases),
        "valid_count": sum(case["valid"] for case in cases),
        "next_case_id": next_case_id(cases),
        "cases": cases,
    }


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=default_repo_root())
    parser.add_argument("--json", action="store_true", help="Emit the complete catalog as JSON")
    parser.add_argument("--strict", action="store_true", help="Fail when any case is incomplete")
    parser.add_argument("--next-id", action="store_true", help="Print only the next available case id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = make_parser().parse_args(argv)
    catalog = build_catalog(args.repo_root.resolve())
    if args.next_id:
        print(catalog["next_case_id"])
    elif args.json:
        print(json.dumps(catalog, ensure_ascii=False, indent=2))
    else:
        for case in catalog["cases"]:
            status = "OK" if case["valid"] else "INVALID"
            print(f"{case['case_id']:>2}  {status:<7}  {case['concept']}  {case['title']}")
        print(f"Cases: {catalog['case_count']} | next id: {catalog['next_case_id']}")

    invalid = [case for case in catalog["cases"] if not case["valid"]]
    if args.strict and invalid:
        for case in invalid:
            print(f"{case['path']}: {'; '.join(case['errors'])}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
