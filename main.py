import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "somethingsomethingidkgmail321@gmail.com" #replace w gmail that u wanna use for spam
EMAIL_PASSWORD = "very cool code 1234" #replace w google app password, search dat shit urself
TO_EMAIL = "veryevilguythatuwanttospam@gmail.com" #replace w the gmail u wanna spam

subject = "Bobliuis" 
body = "hello bro hello helo helo from albanian government"
num_emails = 10 #numbre of gamil u wanna send

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        for i in range(num_emails):
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = TO_EMAIL
            msg["Subject"] = f"{subject} #{i+1}"
            msg.attach(MIMEText(body, "plain"))

            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
            print(f"!!!Email {i+1} sent successfully owo!!!")

except Exception as e:
    print(f"dEmail did not send :(((((: {e}")
