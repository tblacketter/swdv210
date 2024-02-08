#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores_list = []

    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores_list
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores_list.append(score) 
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores_list):
    # calculations
    score_total = sum(scores_list)
    average = round(score_total/len(scores_list))
    sorted_score_list = sorted(scores_list)
    low_score = sorted_score_list[0]
    high_score = sorted_score_list[len(scores_list) - 1]
    median_index = len(sorted_score_list) // 2
    median = sorted_score_list[median_index]
                
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", len(scores_list))
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median)


def main():
    display_welcome()

    scores_list = get_scores()
    process_scores(scores_list)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


