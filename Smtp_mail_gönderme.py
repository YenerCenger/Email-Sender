import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# E-posta iletileri oluşturun
mesaj = MIMEMultipart()
mesaj["From"] = "yener35cenger@gmail.com"
mesaj["To"] = "yenercenger@std.iyte.edu.tr"
mesaj["Subject"] = "Okul Disiplin Kurulu"

yazi = "Merhaba, Lütfen idare ile iletişime geçiniz!"

mesaj_govdesi = MIMEText(yazi, "plain")
mesaj.attach(mesaj_govdesi)

# SMTP sunucusuna bağlanın ve e-postayı gönderin
while True:
    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP sunucu bilgilerinizi ve port numarasını güncelleyin
        mail.ehlo()
        mail.starttls()
        mail.login("yener35cenger@gmail.com", "*****")  # Gönderen e-posta ve şifre
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("E-posta gönderildi.")
        mail.close()
    except Exception as e:
        print("E-posta gönderme hatası:", str(e))