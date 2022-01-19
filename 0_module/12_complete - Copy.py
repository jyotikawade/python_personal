import arithmetic

#entry point function
def main():
	print("enter first number:")
	value1 = int(input())
	
	print("enter second number:")
	value2 = int(input())
	
	ret1= arithmetic.addition(value1,value2)
	ret2= arithmetic.substration(value1,value2)
	
	print("addition is ",ret1)
	print("addition is ",ret2)

#code starter
if (__name__=="__main__"):
	main()
