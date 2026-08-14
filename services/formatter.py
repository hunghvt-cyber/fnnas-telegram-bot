def format_status(data):

    if not data:
        return "Không có dữ liệu."

    text = []

    last = data.get("LAST_UPDATE", "Unknown")

    text.append("🤖 FnNAS Telegram Bot")
    text.append("")
    text.append("🟢 Online")
    text.append("")
    text.append(f"🕒 Last Update")
    text.append(last)
    text.append("")
    text.append("📦 Services")

    for key in [
        "HOMEPAGE",
        "FNNAS",
        "PORTAINER",
        "SFTPGO",
        "FRIGATE"
    ]:

        if data.get(key):
            text.append(f"✅ {key}")

    return "\n".join(text)


def format_urls(data):

    items = [
        ("🌐 Homepage", "HOMEPAGE"),
        ("🖥 FnNAS", "FNNAS"),
        ("📦 Portainer", "PORTAINER"),
        ("📁 SFTPGo", "SFTPGO"),
        ("📹 Frigate", "FRIGATE"),
    ]

    text = []

    for title, key in items:

        text.append(title)
        text.append(data.get(key, "Không có dữ liệu."))
        text.append("")

    return "\n".join(text)