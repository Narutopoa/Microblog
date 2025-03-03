from flask_mail import Message
from flask import render_template
from threading import Thread # Should look into https://flask.palletsprojects.com/en/stable/async-await/

from app import mail, app

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg) # If mail package doesnt handle failure could have infinite running threads

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # If you make your worker threads daemon threads, 
    # they will die when all your non-daemon threads (e.g. the main thread) have exited
    # https://www.geeksforgeeks.org/python-daemon-threads/?ref=ml_lbp
    Thread(target=send_async_email, args=(app, msg), daemon=True).start()