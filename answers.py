# First we open the file we need to use.

file = open('./BobRoss.txt', "r", encoding="utf-8")

fileToUse = file.read().encode("utf-8")

# How many lines does the .txt file have?
# First we split every single line in the text file at their breakpoint, and then we call len() to show the result:

splitByteObject = fileToUse.split(b'\n')

arrayLength = len(splitByteObject)

print("Amount of lines written in the .txt file: " + str(arrayLength))

# How many times does the .txt file write "RUINED" ?
# First we split every single word, and then we do for loop to count the amounts of "RUINED"

arrayOfWords = fileToUse.split(b' ')

count = 0
for word in arrayOfWords:
    if(word == b'RUINED'):
        count += 1

print('The amount of RUINED: ' + str(count))

# How many messages was written after 03:00 ?

splitByteObject = fileToUse.split(b'2015-10-30T03')
messageCounts = len(splitByteObject)

print("Amount of written messages after 03:00: " + str(messageCounts))

# How many different users does the .txt file contain ?

splitByteObject = fileToUse.split(b'\n')

# Get all users
users = []
for line in splitByteObject:
    users.append((line.split(b" ")[1].decode("utf-8")))

# find unique users. Beware! really, REALLY slow solution
def getUniqueUsers(allUsers) :
    uniqueUsers = [] 
    for i in allUsers:
        if not i in uniqueUsers:
            uniqueUsers.append(i)
    return uniqueUsers

print("There is " + str(len(getUniqueUsers(users))) + " unique users")

# What is most used word in the .txt file ?

from collections import Counter
arrayOfWords = fileToUse.split(b' ')
countNumberOneWord = Counter(arrayOfWords).most_common(1)

print("The most used word is: " + countNumberOneWord[0][0].decode("utf-8") + " with an amount of: " + str(countNumberOneWord[0][1]))