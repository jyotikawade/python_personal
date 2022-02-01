class Demo:
	x=10	#class variable shred between all obj
	y=20	#class variable

	def __init__(self): 
		print("inside constructor")
		self.i=30 # instance variable
		self.j=40
	
	def __del__(self):
		print("inside distuctor")
		
	def fun(self):
		print("inside fun")

def main():
	obj1 = Demo() # obj1 is reference which refers to obj of Demo class 
	obj2 = Demo()
	
	obj1.fun() # fun(obj1) 
	
	del obj1	#explicitly if given our function then call to our function 
	del obj2 	#else internally it deletes memory 
	
	#obj1.fun() # fun(obj1) error beacuase  	
		
if __name__=="__main__":
	main()
 	
