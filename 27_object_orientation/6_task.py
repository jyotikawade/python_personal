#design object oriented python application
# and perform below operation
#display all even number 
#calculate the summation of all numbers
#display all perfect number

class Numbers:

	def __init__(self,no=10):
		self.size = no
		self.arr  = []
		
	def Accept(self):
		print("please enter elements")
		for i in range(self.size):
			print("enter number : ",i+1)
			self.arr.append(int(input()))
			
	def Display(self):
		#print("elements of list are")
		#for i in range(self.size):
		#	print(self.arr[i])
		print("elements in lisat are",self.arr,"\n\n")
			
			
	def EvenDisplay(self):
		print("even elements from list are :")
		brr=[]
		for i in range(self.size):
			if(self.arr[i]%2)==0:
				brr.append(self.arr[i])
				
		print(brr)		
		
	def sumation(self):
		sum=0
		for i in range(self.size):
			sum = sum + self.arr[i]
			
		return sum	
			
	def perfectnum(self):
		sum =0 
		brr=[]
		for i in range(self.size):
			for j in range(1,int(self.arr[i]/2)+1): #factor ha ardhya peksha jast yet nahi 16 che fator 8 paryant asnar
				if (self.arr[i]%j)==0:
					sum= sum+j
					
			if sum== self.arr[i]:
				brr.append(self.arr[i])
			
			
			sum =0
		print(brr)
		
	def primenum(self):
		flag = False
		brr=[]
		for i in range(self.size):
			for j in range(2,int(self.arr[i]/2)+1):
				if(self.arr[i]%j)==0:
					flag = True
					break
			if flag == False:
				brr.append(self.arr[i])
			flag = False	
			
		print(brr)	

	def __del__(self):
		print("dealocating the memory of object")
		del self.arr
					
def main():
		print("enter number of elements")
		value=int(input())
		obj1 =Numbers(value)
		obj1.Accept()
		obj1.Display()
		ret = obj1.sumation()
		
		print("sumation of all elements :\n",ret)
		obj1.EvenDisplay()
		
		print("perfect numbers are :")
		obj1.perfectnum()
		print("prime numbers are :")
		obj1.primenum()
		del obj1
		
		
if __name__=="__main__":
	main()
 