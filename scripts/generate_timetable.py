from datetime import datetime, timedelta
from random import choice, randint

def is_empty(day, period):
    if period == 0:
        return True
    elif day == 0 and period in [1, 2, 3, 12, 13, 14]:
        return True
    elif day == 1 and period in range(7, 14):
        return True
    elif day == 2 and period in range(9, 14):
        return True
    elif day == 3 and period in [1, 2, 3, 4, 5, 6]:
        return True
    elif day == 4 and period in [1, 2, 3, 12, 13, 14]:
        return True
    elif day in [5, 6]:
        return True
    return False

def generate_day(day_num, _from, to, empty):
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
    lesson, teacher = choice(lesson_teachers)
    classroom = randint(100, 300)
    now = datetime.now()
    weekday = now.weekday()
    day = now - timedelta(days=weekday) + timedelta(days=day_num)
    day_str = f'<td data-date={day.strftime("%Y-%m-%d")} data-from={_from} data-to={to}  class="line1" id="timetableEntryBox">'
    if empty == False:
        day_str += f"""
  <div class="text"><b>{lesson}</b><br>
        -{teacher} {classroom}</div>
   
    <div class="center plan-lekcji-info"></div>
      <a title=""></a>
        """
    return day_str + '</td>'
def generate_period(period):
    start_period = datetime.now().replace(hour=7, minute=10, second=0, microsecond=0)
    this_period = start_period + timedelta(minutes=45*period)

    if period == 5:
        recess_length = 20
        this_period += timedelta(minutes=10*4)
        this_period += timedelta(minutes=20)
    elif period > 5:
        recess_length = 5
        this_period += timedelta(minutes=5*(period-5))
        this_period += timedelta(minutes=10*4)
        this_period += timedelta(minutes=20)
    else:
        recess_length = 10
        this_period += timedelta(minutes=10*(period))


    if period == 0:
        period_str = ""
    else:
        recess_to = this_period.strftime("%H:%M")
        recess_from = (this_period - timedelta(minutes=recess_length)).strftime("%H:%M")
        period_str = f"""
           <tr class="line0">
            <td class="center">{recess_from}-{recess_to}</td>
          </tr>
          """
    _from = this_period.strftime("%H:%M")
    to = (this_period + timedelta(minutes=45)).strftime("%H:%M")
    period_str += f"""
  <tr class="line1" >
    <td class="center">{period}</td>
    <th class="center border-top">{_from}-{to}</th>
   """ 
    period_str += "".join([generate_day(day, _from, to, empty) for day, empty in [(day, is_empty(day, period)) for day in range(7)]])
    return period_str + '</tr>'

def generate_periods(final_page, periods):
    for period in range(0, periods):
        final_page += generate_period(period)
    return final_page

def generate_timetable():
    final_page = '<table class="decorated plan-lekcji">'
    final_page = generate_periods(final_page, 15)
    return final_page + '</table>'
    
def generate_timetable_html():
    final_page = generate_timetable()
    with open('pages/timetable.html', "w") as timetable:
        timetable.write(final_page)
        timetable.close()

if __name__ == "__main__":
    generate_timetable_html()
