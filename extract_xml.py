import argparse
import shutil
from pathlib import Path


def iter_xml_files(directory: Path):
    """Yield all `.xml` files within `directory` recursively."""
    return (path for path in directory.rglob("*.xml") if path.is_file())


def copy_xml_files(source: Path, destination: Path, overwrite: bool = False) -> int:
    """Copy XML files from `source` to `destination`.

    Returns the number of files copied.
    """
    if not source.is_dir():
        raise NotADirectoryError(f"Source directory not found: {source}")

    destination.mkdir(parents=True, exist_ok=True)

    count = 0
    for xml_file in iter_xml_files(source):
        relative = xml_file.relative_to(source)
        target_path = destination / relative
        target_path.parent.mkdir(parents=True, exist_ok=True)

        if target_path.exists() and not overwrite:
            continue

        shutil.copy2(xml_file, target_path)
        count += 1

    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy all XML files from a source directory into a target directory."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument(
        "--target",
        type=Path,
        default=Path("xml_Dateien"),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    copied = copy_xml_files(args.source, args.target, args.overwrite)
    print(f"Copied {copied} XML file(s) to {args.target}")


if __name__ == "__main__":
    main()