with open('mydata.txt', 'r') as f:
	data = f.read()
	tmp = data.split()
	print('Et011: [%d]' %len(tmp))