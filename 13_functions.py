

#1. function accepts nothing and return nothing
def fun():
	print("in fun")

#2. function which accept parameter and return nothing
def gun(no):
	print("in gun no=",no)

#3. function which accepts parameter and return value
def sun(no):
	print("function sun with parameter:",no)
	return no+1

#4. function accept multiple values and return multiple value
def addsub(no1,no2):
	add = no1+no2
	sub = no1-no2
	return add,sub

#5. nested function

def outerfun():
	print("inside outer")
	def innerfun():
		print("inside inner")
	innerfun()	
	
 
def main():
	fun()
	gun(20)
	ans=sun(30)
	print("in main ans =", ans)
	
	ret1,ret2=addsub(12,10)
	print("addition is=",ret1)
	print("substraction is=",ret2)
	
	outerfun()
	
	
if __name__ =="__main__":
	main()
	