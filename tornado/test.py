# a = 'a '
# b = a.split(' ')
# c = a.strip()
# print(b,c)

a = [1,2]
# b = ''.join(c)
# print(b,c)

list = [str(i) for i in a]
print(list)
b = ''.join(list)
print(b)
c =int(b) +1
d = str(c)
e = [int(k) for k in d]
print(e)
