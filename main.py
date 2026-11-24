"""Write the entry: one line, an AI agent's excuse for breaking production."""
import os
from pathlib import Path

LINE = "I only cleared the cache to make it faster. It turns out the cache was load-bearing."
# 84 characters, well inside the 180-character gate.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
