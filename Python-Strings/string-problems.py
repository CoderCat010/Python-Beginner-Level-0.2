'''
1. Calculate string length.
Write a Python program to calculate the length of a string.
'''
# stringsLength = 'amar sonar bangla'
# print(len(stringsLength))


'''
2. Count character frequency in a string.

Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''
# from collections import Counter
# stringsCollection = 'amazon.com'
# results = Counter(stringsCollection)
# print(dict(results))


'''
3. Get string of first and last 2 chars.

Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''
# getStrings = 'w'
# if len(getStrings) < 2:
#     print('blank')
# else:
#     getResult = getStrings[0:2] + getStrings[-2:]
#     print(getResult)


'''
4. Replace first char occurrences with $.

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t
''' 
# replacement = 'tote'
# firstChar = replacement[0]
# latterCount = replacement[1:] 
# modifytest = latterCount.replace(firstChar ,'$')
# result = firstChar + modifytest

# print(result)


'''
5. Swap first 2 chars of 2 strings.

Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
Click me to see the sample solution
'''

