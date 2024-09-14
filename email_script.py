import weather_script
import json
import ssl
import smtplib
from email.message import EmailMessage

# Grabs temperature data from weather_script.py
data = weather_script.main()

# Creates an empty dictionary for config variables to be stored in
env_config = {}

# Opens the JSON files holding the config information and stores them
# in the env_config dictionary
with open('email_config.json', 'r') as config_json:
    config = json.load(config_json)
    env_config['key'] = config['key']
    env_config['sender'] = config['sender']
    env_config['receiver'] = config['receiver']

# Renames the env_config variables into global variables for ease of use
KEY = env_config['key']
SENDER = env_config['sender']
RECEIVER = env_config['receiver']

# Saves the email subject line in a variable to be called later
email_subject = 'Morning Weather Update'

# Saves the email body in a variable to be called later
email_body_parts = []
for i in range(len(data['act_temp'])):
    email_body_parts.append(f'Temperature of {data['act_temp'][i]}; Feels like {data['feel_temp'][i]}')
email_body = '\n'.join(email_body_parts)

# Creates and sets email settings
email = EmailMessage()
email['From'] = SENDER
email['To'] = RECEIVER
email['Subject'] = email_subject
email.set_content(email_body)

# Creates context to improve email security
context = ssl.create_default_context()

# Logs into gmail account to send morning weather update
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(SENDER, KEY)
    smtp.sendmail(SENDER, RECEIVER, email.as_string())