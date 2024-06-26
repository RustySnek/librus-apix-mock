from generate_grades import generate_grades_html
from generate_notifications import generate_notifications_html
from generate_homework import generate_homework_html
from generate_announcements import generate_announcements_html
from generate_messages import generate_messages_html
from generate_timetable import generate_timetable_html
from generate_attendance import generate_attendance_html
from generate_completed_lessons import generate_completed_html
from generate_schedule import generate_schedule_html
from generate_student_info import generate_student_info_html


def gen_all_html():
    generate_timetable_html()
    generate_schedule_html()
    generate_student_info_html()
    generate_notifications_html()
    generate_homework_html()
    generate_messages_html()
    generate_attendance_html()
    generate_grades_html()
    generate_announcements_html()
    generate_completed_html()


if __name__ == "__main__":
    gen_all_html()
