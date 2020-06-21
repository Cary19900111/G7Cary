import sys

a = [1,2,3,4]
print(sys.getsizeof(a))
b = []
print(sys.getsizeof(b))
b.append(1)
print(sys.getsizeof(b))
b.append(2)
print(sys.getsizeof(b))
b.append(3)
print(sys.getsizeof(b))
b.append(4)
print(sys.getsizeof(b))