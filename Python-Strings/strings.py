# index number
'''x = 'hello'
print(x[3])
'''

# length
'''y = 'HEY!'
print(len(y))'''


# Slicing
names = 'MEGH'

'''print(names[0:3])
print(names[:3])
print(names[2:])'''


# str 
'''
num = 17
convertToString = str(num)

print(convertToString)
print(type(convertToString))
'''


# strip
'''x = ' blue '
removeSpace = x.strip()
print(removeSpace)
'''

# replace
'''repNam = 'hello cat!'
replaceCount = "cat, cat, cat, cat, cat"
replaceWord = repNam.replace('hello', 'Hello')
repCount = replaceCount.replace('cat', 'horse', 3)

print(replaceWord)
print(repCount)
'''


# split
'''spTheName = 'a, b, c, d, e'
countSplitList = 'a, b, c, d, e, f, g, h'
splitToList = spTheName.split(',')
maxSplitList = countSplitList.split(',', 4)

print(splitToList)
print(maxSplitList)
'''


# find
'''findmyWord1 = 'i love icecream'
findmyWord2 = 'i love icecream'
findmyWord3 = 'i love icecream'

find1 = findmyWord1.find("e")
find2 = findmyWord2.find("e", 2)
find3 = findmyWord3.find("e", 13, 15)
print(find1)
print(find2)
print(find3)
'''


# count
'''
countmyWord1 = 'i love icecream'
countmyWord2 = 'i love icecream'
countmyWord3 = 'i love icecream'

count1 = countmyWord1.count("e")
count2 = countmyWord2.count("e", 2)
count3 = countmyWord3.count("e", 12, 15)
print(count1)
print(count2)
print(count3)
'''


# isalpha
'''
alpha1 = 'abc123'
alpha2 = 'abc'
checkIsAlpha1 = alpha1.isalpha()
checkIsAlpha2 = alpha2.isalpha()

print(checkIsAlpha1)
print(checkIsAlpha2)
'''
