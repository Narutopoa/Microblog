from flask_mail import Message
from flask import current_app
from flask_babel import _

from threading import Thread # Should look into https://flask.palletsprojects.com/en/stable/async-await/

from app import mail

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg) # If mail package doesnt handle failure could have infinite running threads

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
    Thread(target=send_async_email,
            args=(current_app._get_current_object(), msg)).start()