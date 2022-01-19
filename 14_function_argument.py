
#positional argument
def student(name,rno,address,marks):
	print("name is= ",name)
	print("rno is= ",rno)
	print("address is= ",address)
	print("marks is= ",marks)
	

#keyword argument
def Computer(RAM,processor,HDD):
	print("RAM size is= ",RAM)
	print("processor name is=  ",processor)
	print("size of HDD id= ",HDD)
	
#default argument	
def circlearea(radius,PI=3.14):
	print("value of PI is =",PI)
	return PI*radius*radius	
	

#variable numner of argument
def fun(*value):
	print("number of argument are",len(value))
	
def main():
	student('jyoti',33,'bhosari',56)
	
	Computer(processor="i7",RAM=8,HDD='1tb')
	Computer(HDD='1tb',processor="i7",RAM=8)
	
	circlearea(1)
	circlearea(1,7.14)
	
	fun(10,20,30)
	fun(19)
	fun(12,2,3,5)
	
	

if __name__=="__main__":
	main()	