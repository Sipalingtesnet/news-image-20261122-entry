#!/usr/bin/env python3
"""main.py — copy entry.png to the output dir, verifying its sha256.

Stdlib only, no network. Deterministic: reads the repo's entry.png and writes
identical bytes to $MAKEFUN_OUTPUT_DIR (or /output/entry.png).
"""
import hashlib
import os
import shutil
import sys

REPO_ENTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")

    digest = sha256(REPO_ENTRY)
    shutil.copyfile(REPO_ENTRY, out_path)

    written = sha256(out_path)
    if written != digest:
        print("ERROR: copied file sha256 mismatch", file=sys.stderr)
        sys.exit(1)

    print(digest)
    sys.exit(0)


if __name__ == "__main__":
    main()