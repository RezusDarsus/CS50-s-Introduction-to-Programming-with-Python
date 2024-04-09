def main():
    user_time_str = input("Enter a time (24-hour format) as # or ##:##: ")
    user_time = convert(user_time_str)
    if 7.0 <= user_time <= 8.0:
        print("It's breakfast time.")
    elif 12.0 <= user_time <= 13.0:
        print("It's lunch time.")
    elif 18.0 <= user_time <= 19.0:
        print("It's dinner time.")

def convert(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60.0



if __name__ == "__main__":
    main()
