def get_day():
    try:
        a = int(input("Press number 1-7: "))
        list = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
        if 1 <= a <= 7:
            print(f"Day of the weak is: {list[a]}")
        else:
            print("E")
    except ValueError as e:
        print(f"This number not included: {e}")
def main():
    get_day()
if __name__=="__main__":
    main()