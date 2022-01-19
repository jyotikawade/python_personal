#named function
def Addition(no1,no2):
	return no1+no2
	

#name = lambda parameters:body 
sum = lambda no1,no2 : no1+no2	 

def main():
	print("enter first number")
	val1= int(input())
	
	print("enter second number")
	val2= int(input())
	
	ret =Addition(val1,val2)
	print("addition is=",ret)

	ret = sum(val1,val2)
	print("addition due to lambda function: =",ret)

if __name__=='__main__':
	main()

