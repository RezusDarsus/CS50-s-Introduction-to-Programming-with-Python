str = input("Write some texts: ")

def convert(str):
    str = str.replace(":)" , "🙂")
    str = str.replace(":(" , " 🙁 ")
    return  str


def main(str):
    print(convert(str))

main(str)