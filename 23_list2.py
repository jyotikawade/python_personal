def Display(List):
	icnt = 0
	sum =0
	for icnt in range(len(List)):
		sum=sum+List[icnt]
	
	return sum	
	
def main():
	Arr = [10,20,30,40,50]
	sum=Display(Arr)
	print("sum=",sum)
	
	
if __name__=='__main__':
	main()		
	 	 	