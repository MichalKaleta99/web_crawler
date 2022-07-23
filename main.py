import wikipedia
wikipedia.set_lang('pl')

crossword_levels=10

def check_validity(word):
    for char in word:
        ascii_char = ord(char)
        if (ascii_char<65 or ascii_char>122):
            return False
    return True

def check_len(word):
    if len(word)>crossword_levels:
        return False
    return True

def choose_first_word():
    headword = wikipedia.random(1)
    while not check_validity(headword):
        headword = wikipedia.random(1)
        print('headword - '+headword)
    if check_len(headword):
        return headword
    else:
        choose_first_word()

def find_next_word(char):
    word = wikipedia.random(1)
    while not check_validity(word):
        word = wikipedia.random(1)
    if (char.lower() or char.upper()) in word:
        return word
    else:
        return None
def define_index(word, char):
    if char.lower() in word:
        char=char.lower()
    if char.upper() in word:
        char=char.upper()
    return word.index(char)
def print_crossword(headword):
    for char in headword:
        word = find_next_word(char)
        while word==None:
            word = find_next_word(char)
        char_index = define_index(word, char)
        print('Słowo - '+word)
        print('_ '*char_index+char+' '+'_ '*(len(word)-1-char_index))

if __name__ == "__main__":
    headword = choose_first_word()
    print_crossword(headword)