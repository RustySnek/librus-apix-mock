from random import choice, randint


def generate_event(num, day_num):
    description = "Placeholder description"
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
    event = f"""
        <td onclick="'//schedule/{num}-{day_num}.html" title="Nauczyciel: {teacher}<br />Opis: {description}">
        : {randint(0,14)}
        <span>{subject}</span>
    """

    return event + "</td>"


def generate_schedule_day(num):
    schedule = f"""
    <div class="kalendarz-dzien">
    """
    schedule += f'<div class="kalendarz-numer-dnia">{num}</div>'
    num_of_events = randint(0, 4)
    schedule += "<tr>"
    schedule += "".join(generate_event(num, n) for n in range(num_of_events))

    schedule += "<tr/>"

    return schedule + "</div>"


def generate_schedule_html():
    days = "".join(generate_schedule_day(n) for n in range(30))
    with open("pages/schedule.html", "w") as schedule:
        schedule.write(days)
        schedule.close()


if __name__ == "__main__":
    generate_schedule_html()
