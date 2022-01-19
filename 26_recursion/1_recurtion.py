def DisplayI(no):
	for i in range(no):   #iterative using for loop
		print("hello")
		

def DisplayW(no):
	while no!=0:
		print('hello')		#iterative using while loop
		no= no-1


def DisplayR(no):
	if no!=0:
		no= no-1			#recursive call
		print("hello")
		DisplayR(no)

def main():
	print("enter the number of iterations")
	value = int(input())
	
	print("calling iterative function")
	DisplayI(value)
	
	print("calling iterative function while loop")
	DisplayW(value)
	
	print("calling recursive function")
	DisplayR(value)
	

if __name__=='__main__':
	main()
	
	
	

	