import os
import smtplib
from email.message import EmailMessage

from main import *
import degiskenler



def send_mail():

  try:

        mail_subject = "Puantaj Kontrol Raporu"
        mail_from = "pythonmailgonderim@gmail.com"
        mail_to = degiskenler.gönderilenler
        mail_mesaj = "Merhaba, ekte puantaj kontrol raporu mevcuttur. İyi Çalışmalar."
        appPassword = "clbj ioyn gmhy pqzp"
        with open("Kontrol_raporu.xlsx", "rb") as f:
            file = f.read()
            file_name = f.name
        mail = EmailMessage()
        mail["Subject"] = mail_subject
        mail["From"] = mail_from
        mail["To"] = mail_to
        mail.set_content(mail_mesaj)
        mail.add_attachment(file, maintype="application", subtype="octet-stream", filename=file_name)
        with smtplib.SMTP_SSL("smtp.gmail.com") as sent:
            sent.login("pythonmailgonderim@gmail.com", appPassword)
            sent.send_message(mail)
            sent.quit()

        print(f"{file_name} isimli dosya mail olarak gönderilmiştir...")

  except Exception as e:
      print(f"{e} Hatası Oluştu..")


if __name__ == "__main__":

    özet_tablo()
    send_mail()