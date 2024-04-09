math = input("Expression: ")
x,y,z =math.split(" ")
x = float(x)
z = float(z)

if(y == "+"):
    result = x + z
elif(y == "-"):
    result = x - z
elif(y == "*"):
    result = x * z
elif  (y == "/"):
    if(z == 0):
        print("error")
    else:
        result = x / z



print(result)