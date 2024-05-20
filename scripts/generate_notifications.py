from random import randint

def generate_notifications():
    return f"""
<a class="id-mock"></a>
<a class='button counter'>{randint(1, 10)}</a>
"""

def generate_notifications_html():
    with open("pages/notifications.html", "w") as schedule:
        schedule.write(generate_notifications())
        schedule.close()

if __name__ == "__main__":
    generate_notifications_html()
