import re
s= input()
x= re.findall('\d+', s)
x= [int(i) for i in x]
print(x)

