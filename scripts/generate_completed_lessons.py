from datetime import datetime
from random import choice


def generate_lesson(date: datetime, num):
    categories = ["Exam", "Quiz", "Homework", "Project", "Presentation"]
    lesson_teachers = [
        ("Mathematics", "Professor Johnson"),
        ("History", "Dr. Patel"),
        ("Physics", "Professor Garcia"),
        ("Literature", "Ms. Thompson"),
        ("Chemistry", "Professor Lee"),
        ("Computer Science", "Mr. Davis"),
        ("Biology", "Dr. Smith"),
        ("Art", "Ms. Rodriguez"),
        ("Geography", "Professor Brown"),
        ("Music", "Mr. Wilson"),
    ]
    lesson = f"""
    <tr>
    <td class="center small">{date.strftime('%Y-%m-%d')}</td>
    <td class="tiny">{date.strftime("%A")}</td>
    <td>{num}</td>
    <td>{', '.join(list(choice(lesson_teachers)))}</td>
    <td>{choice(categories)}</td>
    <td>z_val</td>
        <p class="box">
            <a onclick="///attendance-{num},"></a>
        </p>
    """
    return lesson + "</tr>"


def generate_completed(date: datetime):
    page = f"""
    <table class="decorated">
        <tbody>
    """
    page += "".join(generate_lesson(date, n) for n in range(15))
    return page + "</tbody></table>"


def generate_completed_html():
    now = datetime.now()
    page = generate_completed(now)
    with open("pages/completed.html", "w") as completed:
        completed.write(page)
        completed.close()
