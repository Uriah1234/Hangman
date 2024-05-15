def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()
        print("List of words from file:", words)  # Debug print
    num_unique_words = len(set(words))
    chosen_word = words[(index - 1) % len(words)]
    return num_unique_words, chosen_word

def show_hidden_word(secret_word, old_letters_guessed):
    str = ''
    for i in secret_word:
        if i in old_letters_guessed:
            str += i + ' '
        else:
            str += '_ '
    return str

# Call the function with debug prints
old_letters_guessed = ['e']
num_unique, word = choose_word("words.txt", 3)
print("Number of unique words:", num_unique)
print("Chosen word:", word)
print("word:" , show_hidden_word(word,old_letters_guessed))
