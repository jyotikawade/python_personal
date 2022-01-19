#taking input from user for list and return addition








def main():
	no=int(input("how many elements you want="))
	Arr=[]
	for i in range(no):
		
		Arr.append(input('enter value no{} =  '.format(i)))
	
	print(Arr)
	



	
if __name__=='__main__':
	main()		
	 	 	