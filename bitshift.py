
a = 1      ## 000001
b = a << 1 ## 000010
c = a << 2 ## 000100
d = a << 3 ## 001000

print(a)   ## 1
print(b)   ## 2
print(c)   ## 4
print(d)   ## 8

a = 8      ## 001000
b = a >> 1 ## 000100
c = a >> 2 ## 000010
d = a >> 3 ## 000000

print(a)   ## 8
print(b)   ## 4
print(c)   ## 2
print(d)   ## 1
