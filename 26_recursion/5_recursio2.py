sum=0
i=0
def addition(data):
	sum=0				#iteraton
	for i in range(len(data)):sum= sum+data[i]
		
	return sum	


def additionR(data):
	global sum			#recursion
	global i
	
	if i<len(data):
		sum = sum+data[i]
		i=i+1
		additionR(data)
		
	return sum	

def main():
	arr=[]
	size = int(input("enter the size of array"))
	for i in range(size):arr.append(int(input()))

	print("data is",arr)

	print("addition is",additionR(arr))

if __name__=="__main__":
	main()
	