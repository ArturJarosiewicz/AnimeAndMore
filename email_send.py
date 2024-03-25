import smtplib, ssl

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

sender = "apollonascie@gmail.com"
password = "5qRPt7r5s%"
message = """
Hello!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(sender, password)
    server.send_message(msg=message, from_addr=sender, to_addrs=sender)
