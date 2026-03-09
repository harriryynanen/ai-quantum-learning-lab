from pathlib import Path
import json


def read_json(path: str | Path) -> dict:
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8"))
