from urllib.request import urlopen

BUFSIZE = 256*1024

fileurl = 'https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe'
filename = fileurl.split('/')[-1]
try:
	with urlopen(fileurl) as f:
		with open(filename, 'wb') as h:
			buf = f.read(BUFSIZE)
			while buf:
				h.wirte(buf)
				buf = f.read(BUFSIZE)
except Exception as e:
	print(e)