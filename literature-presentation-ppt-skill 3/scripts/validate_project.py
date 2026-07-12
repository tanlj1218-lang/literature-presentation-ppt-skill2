#!/usr/bin/env python3
"""Validate a project workspace created for the literature-presentation-ppt skill."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED_PATHS = [
    "project-config.yaml",
    "inputs",
    "working/slide_specs",
    "working/evidence-tracker.csv",
    "working/literature-evidence-matrix.csv",
    "outputs/delivery-manifest.md",
]


REQUIRED_LITERATURE_COLUMNS = {
    "database_or_website",
    "search_date",
    "search_terms",
    "source_type",
    "title",
    "authors",
    "year",
    "journal_or_publisher",
    "doi_or_url",
    "full_text_checked",
    "exact_claim_supported",
    "slide_numbers",
    "quality_notes",
}

REQUIRED_EVIDENCE_COLUMNS = {
    "ppt_slide",
    "slide_title",
    "content_type",
    "source_type",
    "source_title",
    "pdf_page",
    "original_table_figure",
    "extraction_method",
    "modified_or_annotated",
    "data_estimated",
    "verification_status",
    "notes",
}


def validate_evidence_tracker(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"Missing evidence tracker: {path}"]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
    missing = REQUIRED_EVIDENCE_COLUMNS - columns
    if missing:
        errors.append(f"Evidence tracker missing columns: {', '.join(sorted(missing))}")
    return errors


def validate_literature_matrix(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"Missing literature evidence matrix: {path}"]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
    missing = REQUIRED_LITERATURE_COLUMNS - columns
    if missing:
        errors.append(f"Literature evidence matrix missing columns: {', '.join(sorted(missing))}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a literature-presentation project workspace.")
    parser.add_argument("project_dir", help="Project directory to validate")
    args = parser.parse_args()

    root = Path(args.project_dir).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        print(f"ERROR: Project directory does not exist: {root}")
        return 2

    for relative in REQUIRED_PATHS:
        if not (root / relative).exists():
            errors.append(f"Missing required path: {relative}")

    errors.extend(validate_evidence_tracker(root / "working/evidence-tracker.csv"))
    errors.extend(validate_literature_matrix(root / "working/literature-evidence-matrix.csv"))

    pdfs = list((root / "inputs").glob("*.pdf")) if (root / "inputs").exists() else []
    if not pdfs:
        warnings.append("No PDF found in inputs/.")

    specs = list((root / "working/slide_specs").glob("*.yaml"))
    if not specs:
        warnings.append("No slide specification YAML files found.")

    pptx_files = list((root / "outputs").glob("*.pptx")) if (root / "outputs").exists() else []
    if not pptx_files:
        warnings.append("No final PPTX found in outputs/.")

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s).")
        return 1

    print(f"Validation passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
