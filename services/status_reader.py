import os

from config.config import STATUS_FILE


def load_status():

    data = {}

    if not os.path.exists(STATUS_FILE):
        return data

    with open(
        STATUS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)

            data[key] = value

    return data