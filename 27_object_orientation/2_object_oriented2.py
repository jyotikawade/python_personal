

def add(no1,no2):
	return no1+no2

def sub(no1,no2):
	return no1-no2

def main():
	val1=int(input("enter first number"))
	val2=int(input("enter second number"))
	
	ret=add(val1,val2)
	print("addition= ",ret)
	
	ret=sub(val1,val2)
	print("substraction= ",ret)


if __name__=="__main__":
	main()
