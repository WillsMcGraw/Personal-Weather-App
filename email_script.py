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
with open('config.json', 'r') as config_json:
    config = json.load(config_json)
    env_config['key'] = config['email_key']
    env_config['sender'] = config['sender']
    env_config['receiver'] = config['receiver']
    env_config['city'] = config['city']
    env_config['state_code'] = config['state_code']

# Renames the env_config variables into global variables for ease of use
KEY = env_config['key']
SENDER = env_config['sender']
RECEIVER = env_config['receiver']
CITY = env_config['city']
STATE = env_config['state_code']

# Saves the email subject line in a variable to be called later
email_subject = 'Morning Weather Update'

# Saves the email body in a variable to be called later
email_body_parts = []
email_body_parts.append(f'Morning weather update for {CITY}, {STATE} on {data['time'][0].strftime('%Y-%m-%d')}')
for i in range(len(data['act_temp'])):
    a_temp = data['act_temp'][i]
    f_temp = data['feel_temp'][i]
    time = data['time'][i].strftime('%H-%M')
    email_body_parts.append(f'\t{time}: {a_temp} F; feels like {f_temp} F')
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