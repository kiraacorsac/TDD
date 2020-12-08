import smtplib
import email.utils
from email.mime.text import MIMEText
import datetime
from AlertHandlers.alert_handler import AlertHandler

# import ssl # Used for secure connection


class Emailer(AlertHandler):
    '''
      handle_alert(alert: Alert):
        Send email, if alert is at least level2

        subject is "Alert"

        content is formatted in the following way:
        'You've got an Alert!
         What: {what}; Where: {where}; Level: {level}' 
   '''

    def __init__(self, source_email, port=1025, server="localhost"):
        self.port = port
        self.smtp_server = server
        self.source_email = source_email

    @property
    def alert_recipient(self):
        return self._alert_recipient

    @alert_recipient.setter
    def alert_recipient(self, recipient):
        self._alert_recipient = recipient

    def _format_message(self, author, recipient, subject, content):
        msg = MIMEText(content)
        msg['From'] = email.utils.formataddr(('Author',  self.source_email))
        msg['To'] = email.utils.formataddr(('Recipient', recipient))
        msg['Subject'] = subject

        return msg.as_string()

    def _send_message(self, recipient, subject, content):
        server = smtplib.SMTP(self.smtp_server, self.port)
        # Uncomment folllowing three lines and the ssl import,
        # if you would like to try with real modern servers

        # context = ssl.create_default_context()        # create secure connection context
        # server.starttls(context=context)              # establish secure connection
        # server.login(sender_email, <PASSWORD>)        # log in
        message = self._format_message(
            self.source_email, recipient, subject, content)
        server.sendmail(self.source_email, [recipient], message)
        server.quit()

    def handle_alert(self, alert):
        if alert.level >= 2:
            content = "You've got an Alert!\nWhat: {}; Where: {}; Level: {}".format(alert.what, alert.where, alert.level)
            self._send_message(self.alert_recipient, "Alert", content)
