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
##############################################################################
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

##############################################################################
def show_hidden_word(secret_word, old_letters_guessed):
    str = ''
    for i in secret_word:
        if i in old_letters_guessed:
            str += i + ' '
        else:
            str += '_ '
    return str
##############################################################################
def check_win(secret_word, old_letters_guessed):
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True
##############################################################################
def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()

    count = len(set(words))

    if index > count:
        index %= count

    return count, words[index - 1]
##############################################################################
def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'l','a','m']
    print(check_win(secret_word, old_letters_guessed))
if __name__ == "__main__":
    main()

