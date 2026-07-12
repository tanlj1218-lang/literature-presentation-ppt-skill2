#!/usr/bin/env python3
"""Initialize a project workspace for the literature-presentation-ppt skill."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


PROJECT_DIRS = [
    "inputs",
    "working/notes",
    "working/slide_specs",
    "working/visual_references",
    "working/extracted_assets",
    "working/redrawn_assets",
    "working/code",
    "outputs",
]


def copy_if_missing(source: Path, destination: Path) -> None:
    if not destination.exists():
        shutil.copy2(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a standard workspace for a 45-minute literature presentation project."
    )
    parser.add_argument("project_dir", help="Directory to create or initialize")
    parser.add_argument(
        "--skill-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to the skill package root",
    )
    args = parser.parse_args()

    project_dir = Path(args.project_dir).expanduser().resolve()
    skill_root = Path(args.skill_root).expanduser().resolve()

    project_dir.mkdir(parents=True, exist_ok=True)
    for relative_dir in PROJECT_DIRS:
        (project_dir / relative_dir).mkdir(parents=True, exist_ok=True)

    templates = skill_root / "templates"
    copy_if_missing(templates / "evidence-tracker.csv", project_dir / "working/evidence-tracker.csv")
    copy_if_missing(templates / "delivery-manifest.md", project_dir / "outputs/delivery-manifest.md")
    copy_if_missing(templates / "slide-spec.yaml", project_dir / "working/slide_specs/slide-001.yaml")
    copy_if_missing(skill_root / "examples/project-config.yaml", project_dir / "project-config.yaml")

    readme = project_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            "# Literature Presentation Project\n\n"
            "1. Put the paper PDF and supplements in `inputs/`.\n"
            "2. Complete `project-config.yaml`.\n"
            "3. Build slide specifications in `working/slide_specs/`.\n"
            "4. Track sources in `working/evidence-tracker.csv`.\n"
            "5. Save final deliverables in `outputs/`.\n",
            encoding="utf-8",
        )

    print(f"Initialized project workspace: {project_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
