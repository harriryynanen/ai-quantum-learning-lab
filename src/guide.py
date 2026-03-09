import json
from pathlib import Path
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parents[1]


def load_text(path: str) -> str:
    return (BASE_DIR / path).read_text(encoding="utf-8")


def load_json(path: str) -> dict:
    return json.loads((BASE_DIR / path).read_text(encoding="utf-8"))


def ask_guide(question: str) -> str:
    client = OpenAI()

    state = load_json("templates/project_state.json")
    catalog = load_json("templates/demo_catalog.json")
    system_prompt = load_text("prompts/guide_system_prompt.md")

    response = client.responses.create(
        model="gpt-5",
        input=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": f"""
Project state:
{json.dumps(state, ensure_ascii=False, indent=2)}

Demo catalog:
{json.dumps(catalog, ensure_ascii=False, indent=2)}

Question:
{question}
""",
            },
        ],
    )
    return response.output_text
