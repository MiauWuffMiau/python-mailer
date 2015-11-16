from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import utils

class Mime(object):

    __msg = MIMEMultipart()

    def __init__(self):
        pass

    def get_headers(self):
        return self.__msg

    def generate_email_body(self, msg):
        self.__msg.attach(MIMEText(str(self.__content), 'plain'))
        text = self.__msg.as_string()
        return text

    def get_sender(self):
        return self.__sender

    def get_receivers(self):
        return self.__receivers

    def set_from(self, sender):
        self.__msg['From'] = sender

    def set_to(self, receiver):
        self.__msg['To'] = receiver

    def set_subject(self, subject):
        subject = str(subject)
        self.__msg['Subject'] = subject

    def set_date(self, date=0):
        if date == 0:
            # set_time_now or time object
            date = utils.formatdate(localtime=True)
        self.__msg['Date'] = date

    def set_text(self, content):
        self.__content = content

