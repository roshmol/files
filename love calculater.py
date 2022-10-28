# write a program that tests the compatibility between two peaple.(Love Calculator)To work out the love score between two peaple:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs
# 2. Then check for the number of times the letters in the word LOVE occurs.Then combine these numbers to make a two digit number
# *For Love Scores less than 10 or greater than 90, the messages should be :"Your score is **x**,you go together like coke and mentos."
# *For Love Scores between 40 and 50, the message should be :"Your score is **y**,you are alright together."
# Otherwise, the message will just be their score.e.g.:Your Score is **z**."
# EXPL: # name1="Angela Yu" name2="Jack Bauer"
# T occurs 0 times R occurs 1 time
# U occurs 2 times E occurs 2 times Total=5
# L occurs 1 time o occurs 0 times V occurs o times E occurs 2 times Total=3
# Love score=53


def love_calculator():
    name1=str(input("enter first name"))
    name2 = str(input("enter second name"))
    word1=['T','R','U','E','t','r','u','e']
    word2=['L','O','V','E','l','o','v','e']
    count1=0
    count2=0
    for i in name1:
        if i in word1:
            count1=count1+1
    for i in name2:
         if i in word1:
             count1=count1+1
    for i in name1:
        if i in word2:
            count2 = count2+1
    for i in name2:
        if i in word2:
            count2= count2+1
    total = int((str(count1)) + (str(count2)))
    if total <10 or total >90:
        print("yoour score is",total, "you go together like coke and mentos.")
    if total >40 and total >50:
        print("yoour score is", total,"you are alright together.")
    else:
        print("your score is",total)

love_calculator()



