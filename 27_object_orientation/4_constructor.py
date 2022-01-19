class arithmatic:
	
	value = 111					#class variable shared between all obj

	def __init__(self,i,j):		#constructor
		print("inside constructor")
		self.no1=i  #class instance variable
		self.no2=j	 #class instance variable	
		
	def add(self):   #instance method
		print("class variable value= ",arithmatic.value)
		print("class variable value= ",self.value)
		return self.no1+self.no2

	def sub(self):   #instance method
		return self.no1-self.no2


def main():	
	
	obj=arithmatic(21,11)  #arithmetic(obj) --> __init__(obj)
	obj1=arithmatic(101,51) #__init__(obj2,101,51)
	
	print("class variable value = ",arithmatic.value)
	print("class variable value = ",obj.value)
	
	ret=obj.add()
	print("addition is =",ret)#ret = add(obj1)
	ret=obj.sub()
	print("substaction is =",ret)#ret = sub(obj1)
	
	
	ret=obj1.add()
	print("addition is =",ret)#ret = add(obj2)
	ret=obj1 .sub()
	print("substaction is =",ret)#ret = add(obj2)
	
	
	
	
if __name__=="__main__":
	main()
 