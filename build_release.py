"""Build the no-install executable with Python's standard library."""
from pathlib import Path
import shutil
import tempfile
import zipapp

root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as folder:
    target = Path(folder)
    shutil.copytree(root / "taxprep", target / "taxprep", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (target / "__main__.py").write_text("from taxprep.cli import main\nraise SystemExit(main())\n", encoding="utf-8")
    zipapp.create_archive(target, root / "taxprep.pyz", interpreter="/usr/bin/env python3",
                          compressed=True)
print(root / "taxprep.pyz")
