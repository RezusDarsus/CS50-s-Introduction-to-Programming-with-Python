ans = input("Greeting: ")

if(ans.lower().startswith("hello")):
    print("$0")
elif(ans.lower().startswith("h")):
    print("$20")
else:
    print("$100")
