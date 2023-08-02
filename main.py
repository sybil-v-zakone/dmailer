from models import Mailer

mailer = Mailer(private_key="")

mailer.send_mail(to=mailer.public_key)
