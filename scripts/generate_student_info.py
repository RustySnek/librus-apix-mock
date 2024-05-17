def generate_student_info():
    page = f"""
    <span class="luckyNumber"><b>11</b></span>
<table class="decorated big center">
<tbody>
<tr class="line1">
<td>Jia Tan</td>
</tr>
<tr class="line1">
<td>1A</td>
</tr>
<tr class="line1">
<td>9</td>
</tr>
<tr class="line1">
<td>John Brown</td>
</tr>
<tr class="line1">
<td>Placeholder school for people specializing\nin placeholders\naddress: placeholder 1234</td>
</tr>

"""

    return page + "</tbody></table>"


def generate_student_info_html():
    page = generate_student_info()
    with open("pages/student_info.html", "w") as info:
        info.write(page)
        info.close()


if __name__ == "__main__":
    generate_student_info_html()
