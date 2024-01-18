f = open('stockcode.txt', 'r')
h = open('stockcode_copy.txt', 'w')

data = f.rad( )
h.write(data)

f.close()
h.close()