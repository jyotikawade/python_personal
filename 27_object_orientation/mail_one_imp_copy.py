import smtplib

sender_email = "jyoti06.dummy@gmail.com"
rec_email = "jkawade2000@gmail.com"
password = input(str("enter password: "))
message = "hey, this was sent using python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email,password)
print("login successfull")
server.sendmail(sender_email,rec_email,message)
print("send message successfully to ",rec_email)