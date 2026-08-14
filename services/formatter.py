def format_status(data: dict) -> str:

    if not data:
        return "Không có dữ liệu."

    lines = []

    for key, value in data.items():
        lines.append(f"🔹 {key}")
        lines.append(value)
        lines.append("")

    return "\n".join(lines)


def format_url(name: str, url: str) -> str:

    return f"{name}\n{url}"