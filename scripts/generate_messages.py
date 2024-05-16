
from random import choice
from generate_grades import datetime, random_date

def generate_message(sent, num):
    message_str = """
     <tr class="line0">
          <td>Tick</td>
          <td></td>
    """

    sent_prefix = ""
    if sent == True:
        sent_prefix = "sent-"

    href = f"////message-{sent_prefix}{num}.html"

    unread = choice(["font-weight: bold", ""]) 
    author = choice(["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Oliver"]) 
    title = f"placeholder title for msg {num}"
    date = random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)).strftime("%Y-%m-%d")
    with open(f'pages/messages/message-{sent_prefix}{num}.html', "w") as msg:
        msg.write(f"""
                  <table class="stretch">
                  <tr>
                  <td class='left'>{author}</td>
                  </tr>
                 <tr>
                  <td class='left'>{title}</td>
                  </tr>
                 <tr>
                  <td class='left'>{date}</td>
                  </tr>
                
                  </table>
<div class='container-message-content'>
                  Example message\n\t\tMessage number {num}\nAuthor: {author}
</div>
                  """)
        msg.close()
    if sent == True:
        message_str += f'<td><a href="{href}">{author}</a></td>'
    message_str += f'''
 <td style={unread}><a href="{href}">{author}</a></td>
          <td>{title}</td>
          <td>{date}</td>
    '''

    return message_str + '<td>Trash</td></tr>'

def generate_messages(sent):
    final_page = f'''
       <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message Mock</title>
</head>
<body>

<table class="decorated stretch">
    <thead>
        <tr>
            <th>Tick</th>
            <th>Attachment</th>
            <th>Author</th>
            <th>Title</th>
            <th>Date</th>
            <th>Trash</th>
        </tr>
    </thead>
    <tbody>
    '''
    final_page += "".join([generate_message(sent, i) for i in range(50)])
    return final_page + f'''
                </tbody>
        </table>

        <div class="pagination">
              <span>Strona 1z1</span>
        </div>

        </body>
        </html>
       '''

def generate_messages_html():
    recieved_final_page = generate_messages(False)

    with open('pages/messages.html', "w") as msgs:
        msgs.write(recieved_final_page)
        msgs.close()
    sent_final_page = generate_messages(True)

    with open('pages/sent_messages.html', "w") as msgs:
        msgs.write(sent_final_page)
        msgs.close()


if __name__ == "__main__":
    generate_messages_html()
