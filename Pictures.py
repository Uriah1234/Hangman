HANGMAN_PHOTOS = {
    1: '''
    x-------x
    '''
    ,
    2: '''
    x-------x
    |
    |
    |
    |
    |
    '''
    ,
    3: '''
    x-------x
    |       |
    |       0
    |
    |
    |
    '''
    ,
    4: '''
    x-------x
    |       |
    |       0
    |       |
    |
    |
    '''
    ,
    5: '''
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    '''
    ,
    6: '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    '''
    ,
    7: '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    '''
}

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

num_of_tries = 6
print_hangman(num_of_tries)


HANGMAN_ASCII_ART = '''Welcome to the game Hangman 
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
