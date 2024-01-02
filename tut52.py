# Regular Expressions 

# Regular expressions are for matching text patterns.
# [] -> Represent a character class
# ^ -> Matches the beginning 
# $ -> Matches the end 
# . -> Matches any character except new line 
# ? -> Matches zero or one occurance
# | -> Means OR(Matches with any of the characters separated by it)
# * -> Any number of occurances(Including 0 occurances)
# + -> One or more occurances
# {} -> Indicate number of occurances of a preceding RE to match
# () -> Enclose a group of REs 

import re
pattern = "[A-Z]+inter"
text = '''Now is the Winter of our discontent Made glorious summer by this sun of York;And all the cloudsthat lour'd upon our houseIn the deep bosom of the ocean buried.Now are our brows bound with victoriouswreaths;Our bruised arms hung up for monuments;Our stern alarums changed to merry meetings,Our dreadfulmarches to delightful measures. Grim-visaged war Dinter hath smooth'd his wrinkled front; And now, instead ofmounting barded steeds To fright the souls of fearful adversaries, He capers nimbly in a lady's chamber Tothe lascivious pleasing of a lute. But I, that am not shaped for sportive tricks, Nor made to court anamorous looking-glass; I, that am rudely stamp'd, and want love's majesty To strut before a wanton amblingnymph; I, that am curtail'd of this fair proportion,'''
match = re.search(pattern, text)
print(match)  #Returns about only the first appeared word with _inter

matches = re.finditer(pattern, text)
for match in matches:
    print(match) # Returns about the appeared word with _inter
    print(match.span()) # Returns the indexes of the words
    print(text[match.span()[0]: match.span()[1]]) # Returns the word with _inter