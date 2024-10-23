import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart

#Set up the SMTP server
smtp_server = 'smtp.gmail.com'
port = 465

#sender email account
sender_email = ''
app_pass = ''

#Create the email
recpient_email = input('Enter the address where you would like the email sent: ')
subject = input('(Optional) Enter a subject title:')

#Allow for multi-line messages
print('\nEnter the message for the email. Once finished, enter an empty line\n')
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)
body = '\n'.join(lines)

# Number of spam e-mails sent
iterations = int(input('Enter the number of times you would like the email sent: '))

#Create a multipart email
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recpient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    # connect to the server and send the email
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, app_pass)
        #send the email for 'iteration' number of times
        for index in range(iterations):
            server.sendmail(sender_email, recpient_email, message.as_string())
        server.quit()
    print('Email sent successfully')
except Exception as e:
    print(f'Error occured: {e}')