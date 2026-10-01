import os

from config.config import STATUS_FILE


def load_status():
    return load_env_file(STATUS_FILE)


def load_env_file(path):
    data = {}

    if not os.path.exists(path):
        return data

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or "=" not in line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            data[key] = value

    return data
