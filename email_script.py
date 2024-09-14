import weather_script
import smtplib
from email.mime.text import MIMEText

# Grabs temperature data from weather_script.py
data = weather_script.main()

# Prints temperature data onto a text file and converts it
# into MIMEText
with open('output.txt', 'w') as my_file:
    # Prints temperature data onto the output file
    for i in range(5):
        my_file.write(f'Temperature: {data['act_temp'][i]}\n')
        my_file.write(f'Feels like: {data['feel_temp'][i]}\n\n')
    # Converts the text file into MIMEText
    email = MIMEText(my_file.read())
    email['Subject'] = my_file.read()
    # Closes output file
    my_file.close()

email['From'] = "wills.mcgraw21@gmail.com"
email['To'] = "wills.mcgraw21@gmail.com"

s = smtplib.SMTP('localhost')
s.sendmail("wills.mcgraw21@gmail.com", ["wills.mcgraw21@gmail.com"], email.as_string())
s.quit()