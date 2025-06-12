import random

# words = ['apple',    'bread','candy',    'dream','eagle','flame','grape','house','input','joker']
words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']

# x = random.random()
# y = x * len(words)
# z = int(y)
# secret_word = words[z]
def choose_the_word(words):
    return random.choice(words)


# if len(guess)!=wl:
#    print("Wrong length. Expected", wl)
#    continue
def valid_guess_len(guess, expected_length):
    return len(guess) == expected_length


# result=[]; i=0
# while i<wl:
#     ch = guess[i]
#     if ch==w[i]:
#         result.append('correct')
#     elif ch in w:
#         result.append('present')
#     else:
#         result.append('absent')
#     i+=1
def evaluate_guess(secret_word, guess):
    result = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            result.append('correct')
        elif guess[i] in secret_word:
            result.append('present')
        else:
            result.append('absent')
    return result

# display=[]
# j=0
# while j<wl:
#     s = guess[j]
#     res = result[j]
#     if res=='correct':
#         display.append("["+s.upper()+"]")
#     elif res=='present':
#         display.append("("+s+")")
#     else:
#         display.append(" "+s+" ")
#     j+=1
def display_result(guess, result):
    display = []
    for letter, res in zip(guess, result):
        if res == 'correct':
            display.append(f"[{letter.upper()}]")
        elif res == 'present':
            display.append(f"({letter})")
        else:
            display.append(f" {letter} ")
    return ' '.join(display) 


# tries = 6
# wl(word length) = len(secret_word)
# w = secret_word -> it is the most pointless
def game_play(words):
    secret_word = choose_the_word(words)
    word_len = len(secret_word)
    tries = 6 
    # print("Welcome to Wordle!") -> that's okay
    print("Welcome to Wordle!")

    # print("Guess the",wl,"-letter word. You have", tries, "tries.")
    print(f"Guess the {word_len}-letter word. You have {tries} tries.")

    # while tries!=0:
    try_num = 0
    while try_num < tries:
        
        # guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
        guess = input(f"Attempt {try_num + 1}/6 – Enter guess: ").lower().strip() 
        # .lower() - it is useful so I leave it
        # .strip() - is useful to prevent unnecessary spaces from the beginning and end

        # We also could use (try: except) - it is useful to prevent invalid input (if smth may happened), but it's unnecessary
            # try:
            #     guess = input(f"Attempt {try_num + 1}/6 – Enter guess: ").lower().strip() 
            # except: 
            #     print("Input error. Please try again.")
            #     continue


        # if len(guess)!=wl:
        #    print("Wrong length. Expected", wl)
        #    continue 
        if not valid_guess_len(guess, word_len):
            print(f"Wrong length. Expected {word_len} letters")
            continue

        # if guess==w:
        #     print("You win!!!")
        #     break
        if guess == secret_word:
            print("You win!!! 🎉")
            return 
        
    # else:
    # final = secret_word
        result = evaluate_guess(secret_word, guess)
        print("Result:", display_result(guess, result))
        try_num += 1
        
    # print("You lose! The word was:", final)
    print("You lose! 😢 The word was:", secret_word)

game_play(words)