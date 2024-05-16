from datetime import datetime, timedelta
from random import choice


def generate_announcement(date, n):
    announcement = """
    <table class="decorated big center printable margin-top">
    """
    title = f"placeholder title {n}"
    announcement += f"""
       <thead>
            <tr>
                <td>{title}</td>
            </tr>
       </thead> 
    """
    author = choice(
        [
            "Emma",
            "Liam",
            "Olivia",
            "Noah",
            "Ava",
            "William",
            "Sophia",
            "James",
            "Isabella",
            "Oliver",
        ]
    )
    announcement += f"""
        <tr class="line0">
            <td>{author}</td>
        </tr>
        <tr class="line0">
            <td>{(date - timedelta(days=n)).strftime("%Y-%m-%d")}</td>
        </tr>
        <tr class="line0">
            <td>Placeholder\n\t\tannouncement content {n}</td>
        </tr>
    """
    return announcement + "</table>"


def generate_announcements_html():
    now = datetime.now()
    page = "".join(generate_announcement(now, n) for n in range(15))
    with open("pages/announcements.html", "w") as announcements:
        announcements.write(page)
        announcements.close()


if __name__ == "__main__":
    generate_announcements_html()
