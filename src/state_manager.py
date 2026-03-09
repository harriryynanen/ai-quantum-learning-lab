import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
STATE_PATH = BASE_DIR / "templates" / "project_state.json"


def load_state() -> dict:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
