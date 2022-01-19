

def Addition(no1,no2):
	return no1+no2

def main():
	print("enter first number")
	val1= int(input())
	
	print("enter second number")
	val2= int(input())
	
	ret =Addition(val1,val2)
	print("addition is=",ret)

if __name__=='__main__':
	main()

