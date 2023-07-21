import smtplib


class Mailer:

    def __init__(self):
        self.my_email = "MeghnadEmailAssistant@gmail.com"
        self.password = "pqoopneaixigaivz"

    # Redundant method
    """def post(self, receiver, message):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=self.my_email, password=self.password)
        connection.sendmail(from_addr=self.my_email, to_addrs=receiver, msg=message)
        connection.close()"""

    def post(self, receiver, message):

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=receiver, msg=message)
