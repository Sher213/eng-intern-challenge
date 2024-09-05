import sys

#define translations
translations = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..',
    '.' : '..OO.O',
    ',' : '..O...',
    '?' : '..O.OO',
    '!' : '..OOO.',
    ':' : '..OO..',
    ';' : '..O.O.',
    '-' : '....OO',
    '/' : '.O..O.',
    '<' : '.OO..O',
    '>' : 'O..OO.',
    '(' : 'O.O..O',
    ')' : '.O.OO.',
    ' ' : '......',
    'CAP' : '.....O',
    'DEC' : '.O...O',
    'NUM' : '.O.OOO'
}

def translate_braille_to_english(string):
    #booleans for setting capitalization, decimal, and number
    isCap = False
    isDec = False
    isNum = False

    #set return string and start of char parsing
    return_string = ''
    char_start = 0

    #loop through string and parse by each 6 chars
    for char_end in range(len(string) + 6)[::6]:
        
        sub = string[char_start:char_end]

        #if found, add key to return string
        for key, value in translations.items():
            if sub == value:
                if key == 'CAP':
                    isCap = True
                elif key == 'DEC':
                    isDec = True
                elif key == 'NUM':
                    isNum = True
                else:
                    if isCap:
                        return_string = return_string + key.upper()
                        isCap = False
                    elif isDec:
                        #decimal fn was not specified
                        return_string = return_string + '.'
                        isDec = False
                        continue
                    elif isNum:
                        if key == ' ':
                            isNum = False
                        #number key will always be second in the list, so grab that
                        key = [k for k, v in translations.items() if v == sub][1]
                        return_string = return_string + key
                    else:
                        return_string = return_string + key
                break
        #move char_start up
        char_start = char_end
    return return_string


def translate_english_to_braille(string):
    #set return string and start of char parsing
    areNewNums = True
    return_string = ''

    for letter in string:
        if letter.isupper():
            return_string = return_string + translations['CAP'] + translations[letter.lower()]
        elif letter == '.':
            return_string = return_string + translations['DEC'] + translations['.']
        elif letter in '1234567890':
            if areNewNums:
                return_string = return_string + translations['NUM'] + translations[letter]
                areNewNums = False
            else:
                return_string = return_string + translations[letter]
        else:
            if letter in translations.keys():
                return_string = return_string + translations[letter]
    
        if letter == ' ':
            areNewNums = True

    return return_string


if __name__ == "__main__":
    if len(sys.argv) > 1:
        string = ' '.join(sys.argv[1:])
        if sorted(set(string)) == ['.', 'O']:
            print(translate_braille_to_english(string))
        else:
            print(translate_english_to_braille(string))