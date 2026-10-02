import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")

DEFAULT_SETTINGS = {"timezone": "Europe/Moscow", "notifications": True}

TIMEZONES = ["Europe/Moscow", "Asia/Tashkent", "Europe/Kiev", "UTC"]


def _load_settings() -> dict:
    if not os.path.exists(SETTINGS_FILE):
        return {}
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def _save_settings(data: dict) -> None:
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_user_settings(user_id: int) -> dict:
    data = _load_settings()
    return data.get(str(user_id), DEFAULT_SETTINGS.copy())


def set_timezone(user_id: int, timezone: str) -> None:
    data = _load_settings()
    user = data.get(str(user_id), DEFAULT_SETTINGS.copy())
    user["timezone"] = timezone
    data[str(user_id)] = user
    _save_settings(data)


def toggle_notifications(user_id: int) -> bool:
    data = _load_settings()
    user = data.get(str(user_id), DEFAULT_SETTINGS.copy())
    user["notifications"] = not user.get("notifications", True)
    data[str(user_id)] = user
    _save_settings(data)
    return user["notifications"]
