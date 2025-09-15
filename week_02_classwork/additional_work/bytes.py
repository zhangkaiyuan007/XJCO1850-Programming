s = "hello"
b = b"hello"           
b2 = s.encode('utf-8') # str -> bytes
s2 = b2.decode('utf-8') # bytes -> str
print(b, b2, s2)   
