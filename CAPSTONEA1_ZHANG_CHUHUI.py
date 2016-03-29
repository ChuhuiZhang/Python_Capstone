# @author Chuhui Zhang (andrewID: chuhuiz)
# File created: Feb 15, 2016
# File commited:
# This program is in support of content analysis.

# Activity 1

def read():
# read text from end user
    fileContent = input("Please input your text within triple quotation marks: ")
    # remove all leading and trailing spaces of the texts
    fileContent = fileContent.strip()

    # remove all symbols and numbers
    fileContent = fileContent.replace(',', ' ')
    fileContent = fileContent.replace('.', ' ')
    fileContent = fileContent.replace(':', ' ')
    fileContent = fileContent.replace(';', ' ')
    fileContent = fileContent.replace('?', ' ')
    fileContent = fileContent.replace('!', ' ')
    fileContent = fileContent.replace('\'', ' ')
    fileContent = fileContent.replace('\"', ' ')
    fileContent = fileContent.replace('<', ' ')
    fileContent = fileContent.replace('>', ' ')
    fileContent = fileContent.replace('-', ' ')
    fileContent = fileContent.replace('$', ' ')
    fileContent = fileContent.replace('1', ' ')
    fileContent = fileContent.replace('2', ' ')
    fileContent = fileContent.replace('3', ' ')
    fileContent = fileContent.replace('4', ' ')
    fileContent = fileContent.replace('5', ' ')
    fileContent = fileContent.replace('6', ' ')
    fileContent = fileContent.replace('7', ' ')
    fileContent = fileContent.replace('8', ' ')
    fileContent = fileContent.replace('9', ' ')
    fileContent = fileContent.replace('0', ' ')

    # split text into individual words
    individualWords = ' '.join(fileContent.split())

    # create a list of tokens
    tokenList = individualWords.split()

    # print list of tokens to end user
    print(tokenList)

    # return list of token to the main function
    return tokenList

# create the main function
def main():
    tokenList = read()

# call the main function
main()   



