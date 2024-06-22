import smtplib
import ssl
#setup port number and server name

smtp_port = 587
smtp_server ="smtp.gmail.com"


email_from="your_email@gmail.com"
email_to="to_email@gmail.com"

pswd=""

#content of messagae
message="Dear god,please help!!!"

simple_email_context=ssl.create_default_context()

try:
    print ("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from,pswd)
    print("Connected server :-)")

    print()
    print("Sending email to - ",email_to)
    TIE_server.sendmail(email_from, email_to, message)
    print("Email successfully sent to -",email_to)

except Exception as e:
    print(e)

finally:
    TIE_server.quit()