def combine_coins(coin, numbers):
    string = ""
    for number in numbers:
        string += coin + str(number) + ", "
    return string[0:-2]

def main():
    money = combine_coins("$", range(5))

if __name__ == "__main__":
    main()