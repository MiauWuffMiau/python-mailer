import smtplib
class SmtpSettings(object):

    __receivers = set()

    def __init__(self):
        pass

    def set_text(self, text):
        self.__text = text

    def set_sender(self, sender):
        self.__from_addr = sender

    def add_receiver(self, receiver):
        self.__receivers.add(receiver)

    def get_sender(self):
        return self.__sender

    def get_receivers(self):
        return self.__receivers

    def set_smtp_domain(self, domain):
        domain = str(domain)
        self.__domain = domain

    def set_smtp_password(self, password):
        self.__password = password

    def set_smtp_port(self, port):
        self.__port = port

    def send_emails(self):
        for addr in self.__receivers:
            server = smtplib.SMTP(self.__domain, self.__port)
            server.starttls()
            server.login(self.__from_addr, self.__password)
            server.sendmail(self.__from_addr, addr, self.__text)
        server.quit()

