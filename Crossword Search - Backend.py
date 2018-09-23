# This function accepts a 2D list of characters like a crossword puzzle and a word (str) as input.
# It searches the ROWS of the 2D list for the word and if it finds a match it returns a list
# containing the row and column index of the start of the match like:
# [[row_index] , [column_index]]
# Otherwise, returns None

def find_word_horizontal (crosswords, word):
    if not crosswords or not word:
        return None
    for index, row in enumerate(crosswords):
        temp_str = ''.join(row)
        if temp_str.find(word) >= 0:
            return [index, temp_str.find(word)]
    return None


# This function accepts a 2D crossword puzzle and a word and searches the columns of the puzzle
# for the inputted word and returns the starting index of the word if found as:
# [row , column] if it doesn't find the word or either of the inputs are empty, it
# returns None

def find_word_vertical (puzzle, word):
    if not puzzle or not word:
        return None
    for column in range (len(puzzle)):
        temp_str = ''
        for row in puzzle:
            temp_str = temp_str + ''.join(row[column])
        if temp_str.find(word) >= 0:
            return [temp_str.find(word), column]
    return None


print('This program accepts a 2D crossword puzzle and a word as input and searches the rows and columns of the puzzle\n'
 'to find a match for the word. If the match is found this program capitalizes the characters of the word in the puzzle\n'
 'and returns the puzzle. If no match is found this program returns the original puzzle.')
print('---------------------------------------------------------------------------------------------------------------')

input('Please press enter when you are ready to begin the program. ')

def capitalize_word_in_crossword(puzzle):
    word = input('Please input the word you would like to search for: ')
    if not puzzle or not word:
        return None
    if find_word_horizontal(puzzle, word) is not None:
        start = find_word_horizontal(puzzle, word)
        row = start[0]
        column = start[1]
        for column_index in range(column, len(word) + column):
            puzzle[row][column_index] = puzzle[row][column_index].upper()
        print('Word found')
        print(puzzle)
    elif find_word_vertical(puzzle, word) is not None:
        start = find_word_vertical(puzzle, word)
        row = start[0]
        column = start[1]
        for row_index in range(row, len(word) + row):
            puzzle[row_index][column] = puzzle[row_index][column].upper()
        print('Word found')
        print(puzzle)
    else:
        print('Word not found')
        print(puzzle)

print ('Here is an example crossword puzzle:',[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']])
print ("Test the program by searching for the word 'cat'")
loop = True
while loop:
    capitalize_word_in_crossword([['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']])
    valid = False
    while not valid:
        y = input('Do you want to search for another word? (Y or N): ')
        if y.lower() == 'y':
            valid = True
            continue
        elif y.lower() == 'n':
            valid = True
            loop = False
        else:
            print('Invalid response, please input either Y for yes or N for no.')
input('Program finished, click close to exit or press enter.')
