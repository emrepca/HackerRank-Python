s = input()
s = int(s)

x = set()

for i in range(s):
    country = input()
    x.add(country)
    
print(len(x))