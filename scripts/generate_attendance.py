from datetime import timedelta, datetime
from random import randint, choice

def generate_attendances(date_str, _type, period):
    _types = {"nb": "unattended", "sp": "late", "u": "excused", "zw":"freed"}
    attendance_str = ''
    subject = choice([ ("Mathematics", "Professor Johnson"),
        ("History", "Dr. Patel"),
        ("Physics", "Professor Garcia"),
        ("Literature", "Ms. Thompson"),
        ("Chemistry", "Professor Lee"),
        ("Computer Science", "Mr. Davis"),
        ("Biology", "Dr. Smith"),
        ("Art", "Ms. Rodriguez"),
        ("Geography", "Professor Brown"),
        ("Music", "Mr. Wilson"),

    ])

    categories = ["Exam", "Quiz", "Homework", "Project", "Presentation"]
    topic = choice(categories)
    excursion = ["nie", "tak"][0]
    href = f"x/y/z/attendance-{date_str}.html/,"
    title = f"Data: {date_str}<br>Rodzaj: {_types[_type]}<br>Lekcja: {subject[0]}<br>Temat zajęć: {topic}<br>Godzina lekcyjna: {period}<br>Czy wycieczka: {excursion}<br>Nauczyciel: {subject[1]}"
    attendance_str += f'<a title="{title}" onclick="{href}">{_type}</a>'
    return attendance_str

def generate_day(initial_date, num, next_sem):
    if randint(0, 5) == 5:
        return ""
    day_str = """
<tr class="line0">
    """
    if num == 1 and next_sem:
        day_str += '<td class="center bolded"></td>'
    date = (initial_date + timedelta(days=num)).strftime("%Y-%m-%d")
    day_str += f'<td >{date}</td>'
    day_str += ''.join(generate_attendances(date, "nb", n) for n in range(randint(7, 15)))
    return day_str + "</tr>"

def generate_semester(initial_date, next_sem):
    return "".join(generate_day(initial_date,n, next_sem) for n in range(25)) 
def generate_attendance():
    final_page = f'''
        <table class="center big decorated">
    '''
    now = datetime.now()
    final_page += generate_semester(now, False) 
    final_page += generate_semester(now + timedelta(days=180), True)

    return final_page + '</table>'

def generate_attendance_html():
    page = generate_attendance()
    with open('pages/attendance.html', "w") as attendance:
        attendance.write(page)
        attendance.close()


if __name__ == "__main__":
    generate_attendance_html()
