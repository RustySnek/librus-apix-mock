from datetime import datetime, timedelta
import os
from random import choice


def generate_homework(date, n):
    category = "placeholder category"
    lesson = f"lesson {n}"
    teacher = choice(
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
    subject = choice(
        [
            "Mathematics",
            "English Language and Literature",
            "Science (Physics, Chemistry, Biology)",
            "History",
            "Geography",
            "Foreign Languages (Spanish, French, German, etc.)",
            "Physical Education (PE)",
            "Art",
            "Music",
            "Computer Science",
            "Economics",
            "Civics or Government",
            "Sociology",
            "Psychology",
            "Health Education",
            "Environmental Science",
            "Business Studies",
            "Literature",
            "Religious Studies",
            "Ethics or Philosophy",
        ]
    )
    homework = f"""
        <tr class="line0">
        <input onclick="'///{n}-homework.html" />
        <td>{lesson}</td>
        <td>{teacher}</td>
        <td>{subject}</td>
        <td>{category}</td>
        <td>{(date - timedelta(days=n)).strftime("%Y-%m-%d")}</td>
        <td>{(date - timedelta(days=n)).strftime("%H:%M:%S")}</td>
        <td>{(date).strftime("%Y-%m-%d")}</td>
        <td>{(date).strftime("%H:%M:%S")}</td>
    """
    with open(f"pages/homework/{n}-homework.html", "w") as h:
        h.write(
            f"""
<div class="container-background">
<tr>
<td>Teacher</td>
<td>{teacher}</td>
</tr>
<tr>
<td>Rest</td>
<td>is</td>
</tr>
<tr>
<td>a</td>
<td>placeholder</td>
</tr>
                </div>
                """
        )
        h.close()
    return homework + "</tr>"


def generate_homeworks():
    page = f"""
    <table class="decorated myHomeworkTable">
    """
    now = datetime.now()
    page += "".join(generate_homework(now, n) for n in range(5))
    return page + "</table>"


def generate_homework_html():
    path = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(path + "/../" "pages/homework", exist_ok=True)

    page = generate_homeworks()
    with open("pages/homework.html", "w") as homework:
        homework.write(page)
        homework.close()


if __name__ == "__main__":
    generate_homework_html()
