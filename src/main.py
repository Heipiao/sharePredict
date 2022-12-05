import json
from send_email import Emails
from db import Database

if  __name__ == '__main__':
    db = Database()
    items = json.loads(db.get_all_output_report_info_daily())
    usernames, emails = db.get_user_info()
    for name,email in zip(usernames, emails):
        email = Emails(items)
        email.send(name,emails)


