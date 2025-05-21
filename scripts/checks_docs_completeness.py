"""A script to check that all functions defined in the source have a section in docs."""

import ast
import logging
import re
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

SRC_DIR = Path("../src")
DOCS_DIR = Path("../docs")


def get_function_names_from_src(src_dir: Path) -> set[str]:
    """Get function names from a source directory."""
    functions = set()

    for py_file in src_dir.rglob("*.py"):
        with open(py_file, encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read(), filename=str(py_file))

                # Only collect top-level (module-level) function definitions
                for node in tree.body:
                    if isinstance(node, ast.FunctionDef):
                        functions.add(node.name)
            except SyntaxError as e:
                logger.warning(f"Skipping {py_file} due to syntax error: {e}")

    return functions


def get_documented_functions_from_docs(docs_dir: Path) -> set[str]:
    """Get names of documented functions from the docs files."""
    doc_pattern = re.compile(r"### \[`(\w+)`\]\[utilsx\.\1\]")
    documented = set()
    for md_file in docs_dir.rglob("*.md"):
        with open(md_file, encoding="utf-8") as f:
            content = f.read()
            documented.update(doc_pattern.findall(content))
    return documented


def main() -> None:
    """The entrypoint to the script."""
    all_functions = get_function_names_from_src(SRC_DIR)
    documented_functions = get_documented_functions_from_docs(DOCS_DIR)

    undocumented = sorted(all_functions - documented_functions)

    if undocumented:
        logger.warning("The following functions are missing from the documentation:")
        for func in undocumented:
            logger.warning(f"- {func}")
        sys.exit(1)
    else:
        logger.warning("✅ All functions are documented.")


if __name__ == "__main__":
    main()
