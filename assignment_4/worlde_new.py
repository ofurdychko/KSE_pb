import random
words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
def choose_the_word(words):
    return random.choice(words)

def valid_guess_len(guess, expected_length):
    return len(guess) == expected_length

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

def game_play(words):
    secret_word = choose_the_word(words)
    word_len = len(secret_word)
    tries = 6
    print("Welcome to Wordle!")
    print(f"Guess the {word_len}-letter word. You have {tries} tries.")
    try_num = 0
    while try_num < tries:
        guess = input(f"Attempt {try_num + 1}/6 – Enter guess: ").lower().strip()
        if not valid_guess_len(guess, word_len):
                print(f"Wrong length. Expected {word_len} letters")
                continue
        if guess == secret_word:
                print("You win!!! 🎉")
                return 
        result = evaluate_guess(secret_word, guess)
        print("Result:", display_result(guess, result))
        try_num += 1
    print("You lose! 😢 The word was:", secret_word)

game_play(words)