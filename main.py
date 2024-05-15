# כל המצבים של האיש התלוי
HANGMAN_PHOTOS = {
    1: '''
    x-------x
    '''
    ,
    2: '''  :(
    
    x-------x
    |
    |
    |
    |
    |
    '''
    ,
    3: '''  :(
    
    x-------x
    |       |
    |       0
    |
    |
    |
    '''
    ,
    4: '''  :(
    
    x-------x
    |       |
    |       0
    |       |
    |
    |
    '''
    ,
    5: '''  :(
    
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    '''
    ,
    6: '''  :(
    
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    '''
    ,
    7: '''  :(
    
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    '''
}

# פונקציה שמקבלת מספר ניסיונות ומדפיסה את המצב הנוכחי של האיש התלוי
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries+1])


#פונקציה שבודקת האם שחקן ניצח
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

# פונקציה שמראה את התהליך ניחושים של השחקן
def show_hidden_word(secret_word, old_letters_guessed):
    str = ''
    for i in secret_word:
        if i in old_letters_guessed:
            str += i + ' '
        else:
            str += '_ '
    return str

# פונקציה שבודקת האם אות שנוחשה היא תקינה
def check_valid_input(letter_guessed, old_letters_guessed):
    # a check to see if the length of the guess is more than 1
    if len(letter_guessed) != 1:
        return False

    # a check to see if the guess is actually a letter
    if not letter_guessed.isalpha():
        return False

    if(letter_guessed.lower() in old_letters_guessed):
        return False

    return True

# פונקציה שמעדכנת את רשימת האותיות שנוחשו
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        if len(old_letters_guessed) > 1:
            for i in old_letters_guessed[:-1]:
                print(i, end=" --> ")
        if old_letters_guessed:  # Checking if the list is not empty
            print(old_letters_guessed[-1])  # Print the last element separately
        return False

# פונקציה שבוחרת מילה מתוך קובץ מילים
def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()
    num_unique_words = len(set(words))
    chosen_word = words[(index - 1) % len(words)]
    return num_unique_words, chosen_word

# Main function
def main():
    # Welcome screen
    HANGMAN_ASCII_ART = '''Welcome to the game Hangman - Uria Cohen
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/
'''
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART , "\n" , MAX_TRIES)

    # Getting the secret word from the player
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    useless , secret_word = choose_word(file_path, index)
    print("\nLet’s start!\n")

    # Initialize variables
    old_letters_guessed = []
    num_of_tries = 0

    # Main game loop
    while num_of_tries < 6:
        # Print hangman status
        print_hangman(num_of_tries)
        print("Number of tries: ",num_of_tries)

        # Print hidden word
        print(show_hidden_word(secret_word,old_letters_guessed))

        # Get player's guess
        letter_guessed = input("Guess a letter: ")

        # Check if the guess is valid and update guessed letters list
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            # Check if the guess is correct
            if letter_guessed.lower() not in secret_word:
                num_of_tries += 1

            # Check if the player won
            if check_win(secret_word, old_letters_guessed):
                print("WIN")
                return
        if num_of_tries ==6:
            break
    # Print hangman status and the hidden word
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))

    # Player loses
    print("LOSE")

# Call the main function
if __name__ == "__main__":
    main()


