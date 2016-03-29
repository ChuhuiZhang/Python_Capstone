# @author Chuhui Zhang (andrewID: chuhuiz)
# File created: Feb 16, 2016
# File commited:
# This program is in support of content analysis.


# Activity 4
def readFile():
    # read an external .txt fle
    speechFile = open('sotu2014_Scrubbed.txt', 'r', encoding='utf-8')
    fileContent = speechFile.read()
    speechFile.close();

    # convert all text to lowercases
    fileContent = fileContent.lower()
    # remove all leading and trailing spaces of the text
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

    # split text into individual words and store them in a big string
    individualWords = ' '.join(fileContent.split())

    # create a list to store all the words
    wordList = individualWords.split()
    # sort the list of words
    wordList.sort()
    # return the word list without any symbol and numbers
    return wordList


# Activity 2
def deleteNoise(wordList5):
    # read the noise file and convert it to a list
    noiseContent = open('noiseFile.txt', 'r', encoding='utf-8')
    noise = noiseContent.read()
    noiseContent.close()
    noiseList = noise.split()

    # read the replacement file and convert it to a lsit
    replaceContent = open('replacementFile.txt', 'r', encoding='utf-8')
    replacementList = replaceContent.readlines()
    replaceContent.close()
    

    # create a new token list to store the text without the noise
    newTokenList = []

    # perform noise delete
    for each in wordList5:
        if each not in noiseList:
            newTokenList.append(each)

    # convert replacement file to a dictionary
    replaceDict = {}
    for each in replacementList:
        tempList = each.split(',')
        replaceDict[tempList[0]] = tempList[len(tempList) - 1].strip('\n')

    # perform replacement
    keys = replaceDict.keys()
    newList = []
    for each in newTokenList:
        if each in keys:
            newTokenList[newTokenList.index(each)] = replaceDict[each] # replace the words

    # sort the list of words alphabetically in ascending order
    newTokenList.sort()

    # convert the sorted list back to a big string
    sortedContent = ' '.join(newTokenList)
    # return the string
    return sortedContent


# Activity 3
def count(cleanContent):
    # make the text all lowercases
    cleanContent = cleanContent.lower()

    # split the text into a list of words
    biglist = cleanContent.split()
    # create a dictionary to store the word : frequency pair
    dictionary = {}
    count = 0
    # start to count
    for each in biglist:
        if (str(each) in dictionary):
            count += 1
            dictionary[each] = count
        else:
            count = 1
            dictionary[each] = count

    # sort the dictionary alphabetically in accending order
    dictionary = sorted(dictionary.items(), key = lambda dictionary : dictionary[0])

    # outprint the word - frequency pair to end user
    for each in dictionary:
        print(each) 

    return dictionary


# Activity 5
def outputFile(frequency):
    # create a new file, and write words to it
    capstoneFile = open('capstone_zhang.txt', 'w')
    # write the word - frequency pair line by line
    for each in frequency:
        capstoneFile.writelines(str(each))
    # close the file
    capstoneFile.close()


def main():
    # Activity 5
    # read the external file and perform preliminary cleaning
    wordList5 = readFile()

    # perform text scrubbing 
    cleanContent = deleteNoise(wordList5)

    # perform frequency count of the words
    frequency = count(cleanContent)

    # output the text to a .txt file
    outputFile(frequency)


# call the main funciton
main()
