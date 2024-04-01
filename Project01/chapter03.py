def main():
    #Opening message
    dashes = "*" * 100

    print(f"{dashes}")
    print("Baseball Team Manager")
    print("Menu Options")
    print("1 - Calcualtae batting average")
    print("2 - Exit Program")
    print(f"{dashes}")
    print()

    while True:
        userChoice = input("Menu option: ")

        if userChoice == "1":
            print("Calcualting batting average...")
            numOfBats = int(input("Official number of at bats: "))
            numOfHits = int(input("Number of hits: "))
            battingAverage = round((numOfHits/numOfBats), 3)
            print(f"batting average is {battingAverage}")
        elif userChoice == "2":
            print("Bye!")
            exit()
        else:
            print("Not a valid option. Please try again")



if __name__ == "__main__":
    main()
    