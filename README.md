# Email Sender

**Turkish (Türkçe)**

## Proje Açıklaması

Bu Python script'i, belirli bir e-posta adresine belirli bir mesajı gönderir. 

## Kullanım

1. Kodu bilgisayarınıza indirin:

    ```bash
    git clone https://github.com/user/email-sender.git
    cd email-sender
    ```

2. Script'i düzenleyin:

    - `mesaj["From"]`: Gönderen e-posta adresi
    - `mesaj["To"]`: Alıcı e-posta adresi
    - `mesaj["Subject"]`: E-posta konusu
    - `yazi`: Gönderilecek mesaj
    - `mail.login("your_email@gmail.com", "your_password")`: Gönderen e-posta adresi ve şifre

3. Script'i çalıştırın:

    ```bash
    python email_sender.py
    ```

4. Program, belirtilen e-posta adresine belirtilen mesajı gönderir.

## Dikkat Edilmesi Gerekenler

- Script, belirli bir e-posta adresine belirli bir mesajı gönderir.
- Gönderen e-posta adresi ve şifresini güvenli bir şekilde saklayın.

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak istiyorsanız, lütfen bir çekme isteği (pull request) açın. Büyük değişiklikler yapmadan önce, lütfen tartışma bölümünde konuyu açın.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için [LİSANS DOSYASI](LICENSE) dosyasını inceleyin.

---

**English**

## Project Description

This Python script sends a specific message to a specific email address.

## Usage

1. Clone the code to your computer:

    ```bash
    git clone https://github.com/user/email-sender.git
    cd email-sender
    ```

2. Edit the script:

    - `mesaj["From"]`: Sender's email address
    - `mesaj["To"]`: Recipient's email address
    - `mesaj["Subject"]`: Email subject
    - `yazi`: Message to be sent
    - `mail.login("your_email@gmail.com", "your_password")`: Sender's email address and password

3. Run the script:

    ```bash
    python email_sender.py
    ```

4. The program sends the specified message to the specified email address.

## Notes

- The script sends a specific message to a specific email address.
- Keep the sender's email address and password secure.

## Contributing

If you want to contribute to this project, please open a pull request. Before making significant changes, please open a discussion in the Issues section.

## License

This project is licensed under the [MIT License](LICENSE). For more information, see the [LICENSE](LICENSE) file.
