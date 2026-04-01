"""skill_box CLI entry point."""

from __future__ import annotations

import argparse
import sys

from skill_box import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="skill_box", description="skill_box CLI")
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.parse_args(argv)
    print("skill_box is installed. Use -h for help.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
