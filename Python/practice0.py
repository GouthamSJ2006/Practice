print('My first code in Python!')
'''
s = 2
p = 6
d = 10
f = 14

print(s + f,p * d,p * s, f / s, d - s, end="\n")
'''
#Basics math calculations
'''
a = 3.14
b = 123
c = 91j
d = 20j
print((a - b,c + d,c / b,d * a))
'''
#Complex and float calculations
'''
a = '1011001'
b = int(a, 2)
print('conterted value: %d'% b, end="\n")
'''
#Converting binary into intergers
'''
c = float(a)
print('converted value: %f'% c, end="\n")
'''
#Converting binary into float
'''
s = '4'
c = ord(s) #Converting into interger
print("converted value: %c"% c, end="\n")

c = hex(73) #Converting into hex number
print("Hex value:"+ c, end="\n")

c = oct(321)
print("Oct value: "+ c, end="\n")
'''
#Converting into other forms of number
'''
s = 'demo'
c = tuple(s) #Converting string into tuple
print("Tuple value: ", c, end="\n")

c = set(s) #Coverting string into set
print("Set value: ", c, end="\n")

c = list(s) #Converting string into list
print("List value: ", c, end="\n")
'''
#Converting string into tuple, set and list

a = 2
b = 3
tup = (('a', 1),('f', 2),('g', 3))

c = complex(1, 2)
print("Converted complex value: ", c, end="\n")

c = str(b)
print("Converted string value: ", c, end="\n")

c = dict(tup)
print("Dictionary value: ", c, end="\n")

#Converting interger into complex, string and dictionary