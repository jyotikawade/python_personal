def Display():
	icnt = 0
	for icnt in range(10,1,-1):
		print(icnt)
		if(icnt==2):
			break
	else:
		print("displyaing if successfully terminated")
	
def main():

	Display()
	
	
if __name__=='__main__':
	main()		
	 	