

file1 = open('C://Users/Staff/Downloads/codingal Html/M23/Codingal.txt',
			'r')
file2 = open('C://Users/Staff/Downloads/codingal Html/M23/CodingalYpdated.txt',
			'w')
for line in file1.readlines():
	
	if not (line.startswith('Coding')):
		
		
		print(line)
		file2.write(line)
file2.close()
file1.close()
