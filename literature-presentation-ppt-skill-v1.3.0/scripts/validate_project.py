#!/usr/bin/env python3
"""Validate a project workspace created for the literature-presentation-ppt skill."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED_PATHS = [
    "project-config.yaml",
    "inputs",
    "working/storyboard/full-deck-blueprint.md",
    "working/slide_specs",
    "working/visual_references/full_slides",
    "working/slide-production-manifest.csv",
    "working/evidence-tracker.csv",
    "working/style_approval/style-approval-brief.md",
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


REQUIRED_PRODUCTION_COLUMNS = {
    "slide_number",
    "slide_title",
    "slide_spec_file",
    "blueprint_approved",
    "image2_prompt_file",
    "image2_reference_file",
    "image2_reference_approved",
    "reconstruction_file_or_slide",
    "full_slide_image_used_as_background",
    "reference_vs_render_compared",
    "academic_qa_status",
    "visual_qa_status",
    "editability_qa_status",
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


def validate_production_manifest(path: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    row_count = 0
    if not path.exists():
        return [f"Missing slide production manifest: {path}"], row_count
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_PRODUCTION_COLUMNS - columns
        if missing:
            errors.append(f"Slide production manifest missing columns: {', '.join(sorted(missing))}")
        for row in reader:
            if any((value or "").strip() for value in row.values()):
                row_count += 1
                if (row.get("full_slide_image_used_as_background") or "").strip().lower() in {"true", "yes", "1"}:
                    errors.append(f"Slide {row.get('slide_number', '?')} uses a full-slide image as background.")
    return errors, row_count


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
    manifest_errors, manifest_rows = validate_production_manifest(root / "working/slide-production-manifest.csv")
    errors.extend(manifest_errors)

    pdfs = list((root / "inputs").glob("*.pdf")) if (root / "inputs").exists() else []
    if not pdfs:
        warnings.append("No PDF found in inputs/.")

    specs = list((root / "working/slide_specs").glob("*.yaml"))
    if not specs:
        warnings.append("No slide specification YAML files found.")

    image_refs = list((root / "working/visual_references/full_slides").glob("*")) if (root / "working/visual_references/full_slides").exists() else []
    image_refs = [p for p in image_refs if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
    if not image_refs:
        warnings.append("No per-slide image2/image_gen full-slide references found.")

    if specs and image_refs and len(specs) != len(image_refs):
        errors.append(f"Slide specification count ({len(specs)}) does not equal image-reference count ({len(image_refs)}).")
    if manifest_rows and specs and manifest_rows != len(specs):
        errors.append(f"Production-manifest row count ({manifest_rows}) does not equal slide-specification count ({len(specs)}).")

    approval = root / "working/style_approval/style-approval-brief.md"
    if approval.exists():
        text = approval.read_text(encoding="utf-8", errors="ignore")
        if "Approved direction:" not in text and "Approved direction：" not in text:
            warnings.append("Style approval brief does not record an approved direction.")

    pptx_files = list((root / "outputs").glob("*.pptx")) if (root / "outputs").exists() else []
    if not pptx_files:
        warnings.append("No final PPTX found in outputs/.")

    montage_files = list((root / "outputs").glob("*montage*")) if (root / "outputs").exists() else []
    if not montage_files:
        warnings.append("No full-deck montage found in outputs/.")

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
