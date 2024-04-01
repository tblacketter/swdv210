def main():
    #Opening message
    dashes = "*" * 100

    print(f"{dashes}")
    print("Baseball Team Manager")
    print("This program calculates the batting average for a player based\non the players official number of at bats and hits")
    print(f"{dashes}")
    print()
    
    name = input("Player's name: ")
    numOfBats = int(input("Official number of at bats: "))
    numOfHits = int(input("Number of hits: "))

    battingAverage = round((numOfHits/numOfBats), 3)

    print(f"{name}'s batting average is {battingAverage}")


if __name__ == "__main__":
    main()