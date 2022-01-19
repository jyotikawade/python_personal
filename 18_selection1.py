#selection1

def check_fun(no):
	if no%2 == 0:
		return 1
	else:
		return 0	
	

def main():
	no1=int(input("enetr no to check"))
	ret=check_fun(no1)
	
	if ret == 1:
		print("no is even")
	else:
		print("no is odd")	

if __name__=='__main__':
	main()