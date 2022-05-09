# Bitwise Operators
"""
Works on Binary
& 	AND
|	OR
^	XOR
~ 	NOT
<<	Zero fill left shift
>>	Signed right shift
"""

a= 10 #1010
b= 11 #1011
print(a&b) #10 - 1010

a= 10 #1010
b= 11 #1011
print(a|b) #11 - 1011

a= 10 #1010
b= 11 #1011
print(a^b) #1 - 0001

a= 10 #1010
b= 11 #1011
print(~b) #b= -(11+1)

a= 10 #1010
b= 11 #1011
print(a<<2) #00001010= 00101000
print(a>>2) #1011= 10.11 = 2