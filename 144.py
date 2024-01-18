with open('stockcode.txt' 't') as f:
	for line_num, line in enumerate(f.readlines()):
		print('%d %s' %(line_num+1, line), end='')
