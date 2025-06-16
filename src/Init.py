"""
Unpack  BPI Challenge 2017.xes.gz  →  BPI Challenge 2017.xes
"""

import gzip
import shutil
from pathlib import Path

SRC  = Path("./DataSet/BPI Challenge 2017.xes.gz")
DEST = Path("./DataSet/BPI Challenge 2017.xes")   # note: same folder, .xes extension

def main() -> None:
    if not SRC.exists():
        raise FileNotFoundError(f"Source file not found: {SRC.resolve()}")

    print(f"Unpacking {SRC.name} → {DEST.name} …")
    with gzip.open(SRC, "rb") as f_in, DEST.open("wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

    print("  Done – unpacked size:", DEST.stat().st_size, "bytes")

if __name__ == "__main__":
    main()
