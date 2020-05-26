import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address="*****@gmail.com"
host_pass="*********"
guest_address="*****@gmail.com"
subject="Status of Success of your model"
content="Failed"
message = MIMEMultipart()
message['From']=host_address
message['To']=guest_address
message['Subject']=subject
message.attach(MIMEText(content,'plain'))
session= smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(host_address,host_pass)
text=message.as_string()
session.sendmail(host_address,guest_address,text)
session.quit()
print("Mail failed")
