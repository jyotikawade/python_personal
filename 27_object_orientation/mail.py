import smtplib		#module for mail functions
				    #extra mail id for practice "jyoti.kawade@t-systems.com",
					# "shubham.yadav@t-systems.com","gauri.mestry@t-systems.com","parth.namdev@t-systems.com"
					#"siddhi.bendkhale@t-systems.com"

sender_email = "jyoti06.dummy@gmail.com"
rec_email = ["jyoti.kawade@t-systems.com","gauri.mestry@t-systems.com","dheeraj.yadav@t-systems.com","siddhi.bendkhale@t-systems.com","parth.namdev@t-systems.com"]

password = input(str("enter password: "))
message = "hey, this was sent using python"


server = smtplib.SMTP('smtp.gmail.com', 587)	#for establishing smtp connection parameter(<server location>,<port to be used>) 
												#for gmail we use 587 port

server.starttls()								#used to inform email server that email client including an email 
												#client running in a web browser wants to turn an existing in secure 								#connection into secure one


server.login(sender_email,password)
print("login successfull")
server.sendmail(sender_email,rec_email,message)
print("send message successfully to ",rec_email)