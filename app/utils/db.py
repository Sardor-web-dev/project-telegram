import json
import os
from datetime import datetime
from json import JSONDecodeError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


def _load_tasks() -> list[dict]:
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="UTF-8") as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []


def _save_tasks(tasks: list[dict]) -> None:
    with open(TASKS_FILE, "w", encoding="UTF-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def create_task(user_id: int, text: str) -> dict:
    tasks = _load_tasks()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {
        "id": new_id,
        "user_id": user_id,
        "text": text,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

    tasks.append(task)
    _save_tasks(tasks)
    return task


def get_tasks(user_id: int, only_activate: bool = True) -> list[dict]:
    tasks = _load_tasks()
    result = [t for t in tasks if t["user_id"] == user_id]
    if only_activate:
        result = [t for t in result if not t["done"]]
        return result

def make_done(user_id: int, task_id:int) -> bool:
    tasks = _load_tasks()
    for t in tasks:
        if t["id"] == task_id and t["user_id"] == user_id:
            t["done"] = True
            _save_tasks(tasks)
            return True
        return False