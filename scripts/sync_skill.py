"""Generate the plugin skill from the root skill; --check never writes files."""

from argparse import ArgumentParser
from pathlib import Path
import shutil
import sys


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated files without changing them")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    plugin_skill = repo / "skills" / "learn-10x"
    sources = [repo / "SKILL.md"]
    for resource in ("agents", "references"):
        sources.extend(sorted(path for path in (repo / resource).rglob("*") if path.is_file()))
    mismatches = []
    expected = set()
    for source in sources:
        relative = source.relative_to(repo)
        destination = plugin_skill / relative
        # Resolve before writing so a misplaced symlink cannot redirect a copy.
        if not destination.resolve().is_relative_to(plugin_skill.resolve()):
            raise ValueError(f"Destination leaves the generated skill folder: {destination}")
        if not plugin_skill.resolve().is_relative_to(repo):
            raise ValueError("Generated skill folder leaves the repository")
        expected.add(relative.as_posix())
        if args.check:
            if not destination.is_file() or source.read_bytes() != destination.read_bytes():
                mismatches.append(relative.as_posix())
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
    extra = []
    if plugin_skill.exists():
        extra = [path.relative_to(plugin_skill).as_posix()
                 for path in plugin_skill.rglob("*")
                 if path.is_file() and path.relative_to(plugin_skill).as_posix() not in expected]
    if mismatches or extra:
        for relative in mismatches:
            print(f"Out of sync: {relative}")
        for relative in extra:
            print(f"Unexpected generated file (not deleted): {relative}")
        return 1
    print(f"{'Checked' if args.check else 'Synced'} {len(sources)} files: skills/learn-10x")
    return 0


if __name__ == "__main__":
    sys.exit(main())
