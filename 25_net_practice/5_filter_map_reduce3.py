#accept n number from user and filter only evern number fro them
#after that add 2 in every even number.
#after the addition of 2 perform summantion 
#of that modified numbers

import functools

CheckEven = lambda no:(no % 2==0)
	
increment= lambda no: no+2
		
add= lambda no1,no2: no1+no2
	
#-----------------------------------------	
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
	newdata=list(filter(CheckEven,arr))
	print("after filtering newdata= ",newdata)
	
	newdata1=list(map(increment,newdata)) #newdata= Map(newdata)
	print("after map data is",newdata1)   #print("after map =",newdata)
	
	output=functools.reduce(add,newdata1)	#addition=reduce(newdata)
	print("after reduce result is= ",output) #print("addition=",addition)


if __name__=='__main__':
	main()








