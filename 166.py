def getTextFreq(filename):
    with open(filename, 'r') as f:
        text = f.read()
        fa = {}
        for c in text:
            if c in fa:
                fa[c] += 1 
            else:
                fa[c] = 1
    return fa

ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key=lambda x: x[1], reverse=True)