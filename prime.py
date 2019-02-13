print("Hello and welcome to tonights edition of....PRIME TIME!!")
print("""This is the ONLY show where you can watch people finding out if a
random number they give us is a prime number or not!  And they say there's
# nothing good on TV anymore!""")

prime = int(input("""Would our first contestant please enter a random number
between 1 and infinity! """))

for number in range(2, prime):
    if prime % number == 0:
        print("Oh, I'm so sorry! That is not a prime number!")
        break
else:
    print("Yeah baby!  You got yourself a prime number!")
