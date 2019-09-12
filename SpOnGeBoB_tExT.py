x=input("Word:")
y=""
for i in range (0,len(x)):
    if i%2==0:
        y+=x[i].upper()
    else:
        y+=x[i].lower()
print(y)
