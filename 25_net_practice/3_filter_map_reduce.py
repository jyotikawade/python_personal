#accept n number from user and filter only evern number fro them
#after that add 2 in every even number.
#after the addition of 2 perform summantion 
#of that modified numbers

#input[1,3,2,4,6,5,4]
#after filter [2,4,6,4]
#after map [2,6,8,6]
#after reduce 24


def CheckEven(no):
	if no % 2==0:
		return True
	else: 
		return False


def myfilter(arr):
	brr=[]
	for i in range(len(arr)):
		if CheckEven(arr[i])== True:
			brr.append(arr[i])
	
	return brr
	
def myMap(arr):
		for i in range(len(arr)):
			arr[i]=arr[i]+2
			
		return arr	
		
def myreduce(arr):
	sum=0
	for i in range(len(arr)):
		sum=sum+arr[i]

	return sum
	
def main():
	arr=[]
	print(" enter the number of elements")
	size = int(input())
	
	for i in range(size):
		print("enter the element no :",i+1)
		value = int(input())
		arr.append(value)

	print("your entered data is",arr)
	
	newdata=myfilter(arr)
	print("newdata= ",newdata)
	
	newdata= myMap(newdata)
	print("after map =",newdata)
	
	addition=myreduce(newdata)
	print("addition=",addition)

if __name__=='__main__':
	main()



