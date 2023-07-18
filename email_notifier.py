import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailNotifier:
    @staticmethod
    def send_email(unused_ips):
        from_email = ""
        to_email = ""
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Unused IP addresses"
        body = "The following IP addresses are unused:\n" + '\n'.join(ip[0] for ip in unused_ips)
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('stmp.com', 587)
        server.starttls()
        server.login(from_email, "pass")
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
