import random
from datetime import datetime, timedelta


# Function to generate a random date
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


# Function to generate a random category
def random_category():
    categories = ["Exam", "Quiz", "Homework", "Project", "Presentation"]
    return random.choice(categories)


# Function to generate a random count to average
def random_count_to_average():
    return random.choice(["Tak", "Nie"])


# Generate td elements
def generate_td_elements(num_elements, teacher, subject):
    td_list = []
    grades = []
    base_href = f"/grades/{subject}/1/"
    for i in range(1, num_elements + 1):
        date = random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)).strftime(
            "%Y-%m-%d"
        )
        category = random_category()
        count_to_average = random_count_to_average()
        grade = random.randint(1, 6)
        if grade == 6:
            grade_text = "6"
            grade_value = 6.0
        elif grade == 1:
            grade_text = "1"
            grade_value = 1
        else:
            if random.choice([True, False]):
                grade_text = str(grade) + "+"
                grade_value = grade + 0.5
            elif random.choice([True, False]):
                grade_text = str(grade) + "-"
                grade_value = grade - 1 + 0.75
            else:
                grade_text = str(grade)
                grade_value = grade
        weight = random.randint(1, 5)
        grades.extend([grade_value] * weight)
        href = f"{base_href}{i}"
        td = f"""
        <td>
          <span class="grade-box" id="grade-box">
            <a href="{href}" title="Data: {date}<br>Kategoria: {category}<br>Nauczyciel: {teacher}<br>Waga: {weight}<br>Licz do średniej: {count_to_average}">{grade_text}</a>
          </span>
        </td>
        """
        td_list.append(td)
    return td_list, grades


def generate_semester(final_page, teacher, num_elements, subject):
    td_elements, grades = generate_td_elements(num_elements, teacher, subject)
    for td in td_elements:
        final_page += td

    # Calculate average of grades
    average_grade = sum(grades) / len(grades)
    average = f"""
      <td class="right">{average_grade:.2f}</td>
      <td class="center">-</td>
      <td class="right">-</td>
    """
    return final_page + average, average_grade


def generate_subject(final_page, subject, teacher, num):
    final_page = '<tr class="line0">'
    final_page += f'<td class="center micro screen-only"></td><td >{subject}</td>'
    final_page, avg1 = generate_semester(final_page, teacher, num, subject)
    final_page, avg2 = generate_semester(final_page, teacher, num, subject)
    final_average = (avg1 + avg2) / 2
    final_page += f'<td class="center">{final_average:.2f}</td>'
    return final_page + "</tr>"


subjects = [
    ("Mathematics", "Professor Johnson", random.randint(4, 15)),
    ("History", "Dr. Patel", random.randint(4, 15)),
    ("Physics", "Professor Garcia", random.randint(4, 15)),
    ("Literature", "Ms. Thompson", random.randint(4, 15)),
    ("Chemistry", "Professor Lee", random.randint(4, 15)),
    ("Computer Science", "Mr. Davis", random.randint(4, 15)),
    ("Biology", "Dr. Smith", random.randint(4, 15)),
    ("Art", "Ms. Rodriguez", random.randint(4, 15)),
    ("Geography", "Professor Brown", random.randint(4, 15)),
    ("Music", "Mr. Wilson", random.randint(4, 15)),
]


def generate_grades_html():
    final_page = ""
    for subject in subjects:
        subject, teacher, num = subject
        final_page += generate_subject("", subject, teacher, num)

    with open("pages/grades.html", "w") as grades:
        grades.write(final_page)
        grades.close()


if __name__ == "__main__":
    generate_grades_html()
