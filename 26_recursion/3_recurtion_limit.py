import sys
	
def main():
	print("recurtion limit is:",sys.getrecursionlimit())
	
	sys.setrecursionlimit(1500)
	
	print("new recurtion limit is:",sys.getrecursionlimit())
	
if __name__=='__main__':
	main()
	
	
	