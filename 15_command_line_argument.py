import sys

def addition():
	sum =0
	for i in range(1,len(sys.argv)):
		sum = sum + int(sys.argv[i])
		
	return sum	
	
def main():
	print("in main")
	sum1=addition()
	print(sum1)
if __name__=='__main__':
	main()
	