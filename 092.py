txt = 'A lot of things occur each day, ever day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
print(offset1)
print(offset2)
print(offset3)