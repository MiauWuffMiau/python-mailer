from libs import mime_mailer
from libs import smtpsettings_mailer

def sending_email():

    mime = mime_mailer()

    mime.set_from("test")
    mime.set_to("test1")
    mime.set_date()
    mime.set_subject("Testing whether its working")
    mime.set_text("Yo")
    
    msg = mime.get_headers()
    text = mime.generate_email_body(msg)

    s = smtpsettings_mailer()
    s.set_text(text)
    s.set_smtp_domain("stmp_domain.com")
    s.set_smtp_password("password")
    s.set_smtp_port(587)
    s.set_sender("test_sender@test.com")
    s.add_receiver("test_receiver@test.com")
    s.send_emails()