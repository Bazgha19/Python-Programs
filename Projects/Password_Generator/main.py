import random

var="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`~@#$%^&*()_+-|}{\][:;'.,<>/?"

length=8

p=''.join(random.sample(var,length))

print(p)

