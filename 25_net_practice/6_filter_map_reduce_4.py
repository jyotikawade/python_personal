import functools
	
def main():
	arr=[]
	print(" enter the number of elements")
	size = int(input())
	
	for i in range(size):
		print("enter the element no :",i+1)
		value = int(input())
		arr.append(value)

	print("your entered data is",arr)
	#syntax:= newdata=filter(function name,list)
	newdata=list(filter(lambda no:(no % 2==0),arr))
	print("after filtering newdata= ",newdata)
	
	newdata1=list(map(lambda no: no+2,newdata)) #newdata= Map(newdata)
	print("after map data is",newdata1)   #print("after map =",newdata)
	
	output=functools.reduce(lambda no1,no2:no1+no2,newdata1)	#addition=reduce(newdata)
	print("after reduce result is= ",output) #print("addition=",addition)


if __name__=='__main__':
	main()








