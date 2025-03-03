set FLASK_APP=microblog.py
set SECRET_KEY=default
set DATABASE_URL=default
set FLASK_DEBUG=0 # Set to 1 to enable, emails will not send in debug mode

#Testing email server
# set MAIL_SERVER=localhost
# set MAIL_PORT=8025

set MAIL_SERVER=smtp.googlemail.com
set MAIL_PORT=587
set MAIL_USE_TLS=1
set MAIL_USERNAME=<your-gmail-username>
set MAIL_PASSWORD=<your-gmail-password>