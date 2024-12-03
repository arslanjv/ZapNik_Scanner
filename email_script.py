import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


def send_email(config, output_file):
    try:
        smtp_server = config.get("smtp_server")
        smtp_port = config.get("smtp_port")
        sender_email = config.get("sender_email")
        app_password = config.get("app_password")
        recipient_email = config.get("recipient_email")

        if not all([smtp_server, smtp_port, sender_email, app_password, recipient_email]):
            raise ValueError("Incomplete email configuration.")

        subject = "ZapNik Vulnerability Scan Results"
        body = "Scan completed successfully. Please find the attached results." 

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with open(output_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(output_file)}"
        )
        message.attach(part)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"Email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")
