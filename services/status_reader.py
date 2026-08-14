import os

from config.config import STATUS_FILE


def load_status():

    result = {}

    if not os.path.exists(STATUS_FILE):
        return result

    with open(STATUS_FILE, "r") as f:

        for line in f:

            line = line.strip()

            if "=" not in line:
                continue

            k, v = line.split("=", 1)

            result[k] = v

    return result