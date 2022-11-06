import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


msg_str = 'this is a test email sending by python'
msg = MIMEText(msg_str, 'plain', 'utf-8')
msg['From'] = 'suite@scf.com'
msg['To'] = 'liny@shinetechsoftware.com'
msg['Subject'] = Header('python email test', 'utf-8').encode()

smtp = smtplib.SMTP('smtp.office365.com',587)
smtp.set_debuglevel(2)
smtp.starttls()
smtp.login('suite@scf.com', 'SCF@almaden99')
smtp.sendmail('suite@scf.com', 'liny@shinetechsoftware.com', msg.as_string())
smtp.quit()
