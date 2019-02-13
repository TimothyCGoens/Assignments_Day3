print("""YAAAAAAAAAHHHH!!!! Is everyone excited tonight?!!  You should be!
You've heard of the Thunderdome?  Well, this is the...PALINDROME!!!!""")
print("Only the fiercest warriors can survive this literary gauntlet.")
print("""In order to become the Champion of the Palindrome, you have to give us
a word that is a palindrome!  This competition isn't for the faint of heart
or the bereft of vocabulary!!!""")

guess = input("What is your word, scrub? ")

def palindrome(word):
    if word == word[::-1]:
        print(f"{word} is a palindrome!! You are the winner!!")
    else:
        print(f"{word} is NOT a palindrome! You lose....YOUR HEAD!")

palindrome(guess)


play_again = input("Would you like one more chance?  y/n ")

if play_again == 'y':
    guess_again = input("Give me another word then! ")
    palindrome(guess_again)
elif play_again == 'n':
    print("Prolly a wise choice for such a weakling!")
