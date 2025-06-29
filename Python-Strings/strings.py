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
spTheName = 'a, b, c, d, e'
countSplitList = 'a, b, c, d, e, f, g, h'
splitToList = spTheName.split(',')
maxSplitList = countSplitList.split(',', 4)

print(splitToList)
print(maxSplitList)